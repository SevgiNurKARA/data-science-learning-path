# 📙 Seviye 3: Makine Öğrenmesi

Bu seviye, makine öğrenmesi algoritmalarını, model değerlendirme tekniklerini ve gerçek projeleri kapsar.

## 🎯 Öğrenme Hedefleri

Bu seviyeyi tamamladıktan sonra:
- ✅ Karar ağaçları ve Naive Bayes gibi algoritmaları anlayabilirsiniz
- ✅ Veri ön işleme tekniklerini derinlemesine uygulayabilirsiniz
- ✅ Model performansını değerlendirebilirsiniz
- ✅ Gerçek veri setleri ile proje yapabilirsiniz
- ✅ Kütüphane kullanmadan preprocessing yapabilirsiniz (from scratch)

## 📚 İçerik Yapısı

### 🌳 Decision Tree

Karar ağaçları algoritması:

- `heartdisease.ipynb` - Kalp hastalığı veri seti ile karar ağacı uygulaması

### 📊 Naive Bayes

Naive Bayes algoritması:

- `heartdisease-nb.ipynb` - Kalp hastalığı veri seti ile Naive Bayes uygulaması

### 🔧 Preprocessing From Scratch

Kütüphane kullanmadan veri ön işleme (from scratch):

#### Data Encoding
- `data_encoding_part1.py` - Veri kodlama
- `data_encoding_part1_PseudoCode.docx` - Pseudo kod
- `p1_data.txt` - Örnek veri

#### Discretization
- `equal_width.py` - Eşit genişlikte discretization
- `input_data.txt`, `output_data.txt` - Giriş/çıkış verileri

#### k-Means
- `k_mean.py` - k-Means kümeleme algoritması
- `data.txt`, `output.txt`, `results.txt` - Veri ve sonuçlar

#### Missing Value
- `missing_value_in_same_class.py` - Aynı sınıftaki eksik değerleri doldurma
- `matrix.py` - Matris işlemleri
- `missing_value_pseudoCode.docx` - Pseudo kod
- `p2_data.txt`, `p2_output.txt` - Veri ve çıkış

#### Oversampling
- `oversampling.py` - Oversampling tekniği
- `data.txt`, `output.txt`, `results.txt` - Veri ve sonuçlar

### 🚀 ML Article Project

Kapsamlı makine öğrenmesi projesi:

#### Veri Setleri
- **Hava Kirliliği** (`updated_pollution_dataset.csv`)
- **Öğrenci Akademik Başarıları** (`student_lifestyle_dataset.csv`)
- **Hava Koşulları** (`weather_forecast_data.csv`)

#### Kullanılan Yöntemler

**Eksik Veri Doldurma:**
- Ortalama ile doldurma (Mean Imputation)
- Mod ile doldurma (Mode Imputation)
- K-Nearest Neighbors (KNN) ile doldurma
- Çoklu atama (Multiple Imputation)

**Dengesiz Veri Setlerini Dengeleme:**
- SMOTE (Synthetic Minority Over-sampling Technique)

**Makine Öğrenmesi Algoritmaları:**
- KNN (K-Nearest Neighbors)
- Naïve Bayes
- Decision Tree (Karar Ağacı)

#### Performans Metrikleri
- **MAE** (Mean Absolute Error)
- **MSE** (Mean Squared Error)
- **Pearson Korelasyonu**
- **Accuracy, Precision, Recall, F1-Score**

#### Dosya Yapısı
- `preprocessing.py` - Veri ön işleme
- `knn.py` - KNN algoritması
- `naive_bayes.py` - Naive Bayes algoritması
- `tree.py` - Decision Tree algoritması
- `best_result.py` - En iyi sonuçları bulma
- `missing_data_files/` - Eksik verilerle test edilen veri setleri
- `completed_data/` - İmputation sonrası tamamlanmış veri setleri
- `output/`, `output_folder/`, `result/` - Performans sonuçları

## 🚀 Nasıl Başlanır?

1. **Algoritmaları öğrenin:**
   - `decision_tree/heartdisease.ipynb` ile başlayın
   - `naive_bayes/heartdisease-nb.ipynb` ile devam edin

2. **From scratch preprocessing:**
   - `preprocessing_from_scratch/` klasöründeki her teknik için Python dosyalarını inceleyin
   - Pseudo kod dosyalarını okuyun

3. **Gerçek proje:**
   - `ml_article_project/` klasöründeki projeyi adım adım takip edin
   - Farklı imputation yöntemlerini karşılaştırın
   - Model performanslarını analiz edin

## ✅ Kontrol Listesi

- [ ] Decision Tree notebook'u çalıştırıldı ve anlaşıldı
- [ ] Naive Bayes notebook'u çalıştırıldı ve anlaşıldı
- [ ] Preprocessing from scratch teknikleri öğrenildi
- [ ] ML Article projesi tamamlandı
- [ ] Farklı imputation yöntemlerinin performansları karşılaştırıldı
- [ ] Model metrikleri yorumlandı

## 📊 Proje Önerileri

1. **Kendi Veri Setinizle Proje:**
   - Kendi veri setinizle eksik veri doldurma tekniklerini uygulayın
   - Farklı ML algoritmalarını deneyin
   - Performansları karşılaştırın

2. **From Scratch Uygulama:**
   - Kütüphane kullanmadan kendi preprocessing fonksiyonlarınızı yazın
   - Algoritmaları from scratch implement edin

## 🎓 İleri Seviye Konular

- Ensemble yöntemleri (Random Forest, Gradient Boosting)
- Hyperparameter tuning
- Cross-validation teknikleri
- Feature engineering
- Model interpretability

## 🔗 Sonraki Adımlar

Bu seviyeyi tamamladıktan sonra:
- Daha karmaşık ML projelerine geçebilirsiniz
- Deep Learning'e başlayabilirsiniz
- Kaggle yarışmalarına katılabilirsiniz

---

**Tebrikler!** 🎉 Veri bilimi öğrenme yolunuzu tamamladınız!

