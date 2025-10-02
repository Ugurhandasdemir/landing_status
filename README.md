# UAP İniş Alanı Uygunluk Kontrolü

Bu proje, bilgisayarla görme (Computer Vision) teknikleri kullanarak iniş alanlarının uygunluğunu tespit etmeyi amaçlamaktadır. Özellikle **uai** (Uçuşa Engel Alan İmajı) ve **uap** (Uçuşa Engel Alan Pikseli) kategorilerinde algılanan nesneler üzerinde çalışır. Eğer iniş alanında engel tespit edilirse alan **inişe uygun değil** olarak işaretlenir.

## Özellikler

- Nesne algılama sonuçları üzerinden iniş alanı değerlendirmesi yapar.
- Algılanan nesnelerin koordinatları kullanılarak alanlar kırpılır.
- İnişe uygunluk, görüntü işleme yöntemleriyle kontrol edilir:
  - Otsu eşiği ile ikili görüntüleme
  - Morfolojik kapanma (morph close) filtresi
  - Kontur (contour) analizi
- Alan üzerinde beyaz piksel yoğunluğu incelenerek inişin güvenli olup olmadığı belirlenir.

## Kullanılan Teknolojiler

- **Python**
- **OpenCV (cv2)**
- **NumPy**


![Sonuç](https://github.com/Ugurhandasdemir/landing_status/blob/main/Screenshot%20from%202025-10-02%2023-30-11.png)
