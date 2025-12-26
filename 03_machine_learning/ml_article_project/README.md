# README - Veri Ön İşleme ve Model Değerlendirme

## Proje Açıklaması
Bu proje, hava kirliliği, öğrencilerin akademik başarılarını etkileyen faktörler ve hava koşulları ile ilgili üç farklı veri setine veri ön işleme adımları uygulayarak eksik verileri doldurmayı, veri dengesizliğini gidermeyi ve farklı makine öğrenimi algoritmaları ile performans değerlendirmesi yapmayı amaçlamaktadır.

## Kullanılan Yöntemler ve Araçlar
- **Eksik Veri Doldurma Yöntemleri:**
  - Ortalama ile doldurma (Mean Imputation)
  - Mod (En sık görülen değer) ile doldurma (Mode Imputation)
  - K-Nearest Neighbors (KNN) ile doldurma
  - Çoklu atama (Multiple Imputation)

- **Dengesiz Veri Setlerini Dengeleme:**
  - **SMOTE (Synthetic Minority Over-sampling Technique)** ile azınlık sınıfı örneklerinin artırılması

- **Makine Öğrenimi Algoritmaları ile Performans Değerlendirme:**
  - **KNN (K-Nearest Neighbors)**
  - **Naïve Bayes**
  - **Decision Tree (Karar Ağacı)**

## Veri Setleri
1. **Hava Kirliliği**: Hava kalitesi ile ilgili parametreleri içeren veri seti.
2. **Öğrenci Akademik Başarıları**: Öğrencilerin akademik performanslarını etkileyen faktörleri içeren veri seti.
3. **Hava Koşulları**: Günlük hava tahmin verilerini içeren veri seti.

## Uygulanan Veri Ön İşleme Adımları
1. **Eksik Veri Analizi**: Eksik verilerin tespiti ve oranlarının belirlenmesi.
2. **Eksik Veri Ekleme**: Rastgele eksik veriler oluşturularak imputation yöntemlerinin performansını ölçmek için test ortamı hazırlandı.
3. **Eksik Veri Doldurma**: Belirlenen eksik veri doldurma yöntemleri ile eksik değerler tamamlandı.
4. **SMOTE Uygulaması**: Dengesiz veri setlerine SMOTE uygulanarak sınıf dengesizliği giderildi.
5. **Makine Öğrenimi Modellerinin Eğitilmesi ve Değerlendirilmesi**: Her veri seti için farklı imputation yöntemleri ile tamamlanmış veri setleri kullanılarak KNN, Naïve Bayes ve Decision Tree algoritmaları eğitildi ve performansları ölçüldü.

## Performans Değerlendirme
Eksik veri doldurma yöntemlerinin doğruluğunu değerlendirmek için aşağıdaki metrikler kullanılmıştır:
- **MAE (Mean Absolute Error - Ortalama Mutlak Hata)**
- **MSE (Mean Squared Error - Ortalama Kare Hata)**
- **Pearson Korelasyonu**

Makine öğrenimi modellerinin performansı aşağıdaki metriklerle ölçülmüştür:
- **Accuracy (Doğruluk Oranı)**
- **Precision (Kesinlik)**
- **Recall (Duyarlılık)**
- **F1-Score**

## Çıktılar ve Sonuçlar
- Eksik veri doldurma yöntemleri arasında en yüksek başarı oranı **Multiple Imputation** yöntemiyle elde edildi.
- **SMOTE** uygulandıktan sonra sınıf dengesizliği giderildi ve model performansında iyileşmeler gözlemlendi.
- **Decision Tree**, belirli veri setleri için en yüksek doğruluğu sağlarken, **Naïve Bayes** düşük boyutlu ve kategorik veri setlerinde daha iyi performans gösterdi.
- **KNN**, eksik verileri KNN imputation ile doldurduğumuz veri setlerinde iyi performans gösterdi.

## Dosya Yapısı
```
.
├── missing_data_files/                # Eksik verilerle test edilen veri setleri
│   ├── weather_forecast_data.csv
│   ├── air_pollution_data.csv
│   ├── student_academic_data.csv
│
├── completed_data/                    # İmputation sonrası tamamlanmış veri setleri
│   ├── weather20_mean_smote.csv
│   ├── weather40_knn_smote.csv
│   ├── air_pollution60_multiple_imputation_smote.csv
│   ├── ...
│
├── scripts/                           # Python betikleri
│   ├── missing_data_processor.py      # Eksik veri işleme ve modelleme kodları
│
└── README.md                          # Bu dosya
```

## Kullanım Talimatları
1. **Bağımlılıkları yükleyin:**
   ```bash
   pip install numpy pandas scikit-learn imbalanced-learn scipy
   ```
2. **Kodları Çalıştırın:**
   ```bash
   python scripts/missing_data_processor.py
   ```

## İletişim
Herhangi bir sorunuz veya öneriniz olursa benimle iletişime geçmekten çekinmeyin.

