import cv2
import numpy as np

def uap(image, prediction_list):
    count = False #True ise inişe uygun değil
    for object in prediction_list:
        if (object.category.name == 'uai') or (object.category.name == 'uap'):
            x0, y0, w, h = map(int, object.bbox.to_xywh())
            x1 = x0 + w
            y1 = y0 + h
            cropped_image = image[y0:y1, x0:x1]

            for object in prediction_list:
                object_x0, object_y0, object_w, object_h = map(int, object.bbox.to_xywh())
                object_x1 = object_x0 + object_w
                object_y1 = object_y0 + object_h

                if (object_x0 > x0 and object_x0 < x1) or (object_x1 > x0 and object_x1 < x1):
                    if (object_y0 > y0 and object_y0 < y1) or (object_y1 > y0 and object_y1 < y1):
                        count = True
                        print("İnişe uygun değil")
                        break

                if (count != True):
                    if object.category.name == "uap":
                        _, binary = cv2.threshold(cropped_image[:, :, 0], 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU, image)

                    if object.category.name == "uai":
                        _, binary = cv2.threshold(cropped_image[:, :, 2], 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU, image)

                        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
                        closed_img = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
                        # find all contours in the binary image and check if there is any white pixels bigger than 15 in largest contour
                        contours, hierarchy = cv2.findContours(closed_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                        largest_contour = max(contours, key=cv2.contourArea)
                        mask = np.zeros_like(closed_img)
                        mask = cv2.fillPoly(mask, pts=[largest_contour], color=(255, 255, 255))
                        n_cls_img = cv2.bitwise_not(closed_img)
                        final_mask = cv2.bitwise_and(n_cls_img, mask)

                        if np.count_nonzero(final_mask) > 20:
                            print("değil")
                            count = True
                        else:
                            print("uygun")
                            count = False
                else:
                    print("girmedi")
