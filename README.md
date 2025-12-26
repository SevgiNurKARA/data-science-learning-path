# 📚 Data Science Learning Path

Sıfırdan veri bilimine başlamak isteyenler için kapsamlı bir öğrenme yolu. Bu repo, NumPy ve Pandas temellerinden başlayarak, veri analizi ve makine öğrenmesine kadar uzanan adım adım bir rehber sunar.

## 🎯 Öğrenme Yolu

| Seviye | Klasör | Konular | Tahmini Süre | Önkoşullar |
|--------|--------|---------|--------------|------------|
| **1** | `01_numpy_pandas` | NumPy & Pandas temelleri, veri manipülasyonu | 3-5 gün | Python temelleri |
| **2** | `02_data_analysis_for_beginners` | Veri görselleştirme, EDA, SciPy, Scikit-learn | 5-7 gün | Seviye 1 tamamlanmış olmalı |
| **3** | `03_machine_learning` | ML algoritmaları, preprocessing, model değerlendirme, feature engineering, hyperparameter tuning | 8-12 hafta | Seviye 2 tamamlanmış olmalı |

## 🚀 Başlangıç

### Gereksinimler

- Python 3.7+
- Jupyter Notebook veya JupyterLab
- Git

### Kurulum

```bash
# Repoyu klonla
git clone https://github.com/SevgiNurKARA/data-science-learning-path.git
cd data-science-learning-path

# Bağımlılıkları yükle
pip install -r requirements.txt

# Jupyter Notebook'u başlat
jupyter notebook
```

## 📖 İçerik Yapısı

### 📘 Seviye 1: NumPy & Pandas

**Klasör:** `01_numpy_pandas/`

- NumPy array'leri ve temel işlemler
- Pandas Series ve DataFrame
- Veri okuma, yazma ve manipülasyon
- Gerçek veri setleri ile çalışma (NBA oyuncu verileri)
- Veri görselleştirme temelleri

**Öğrenme Hedefleri:**
- ✅ NumPy array'leri ile çalışabilme
- ✅ Pandas ile veri analizi yapabilme
- ✅ CSV dosyalarını okuyup işleyebilme
- ✅ Temel veri manipülasyon tekniklerini uygulayabilme

### 📗 Seviye 2: Veri Analizi & Görselleştirme

**Klasör:** `02_data_analysis_for_beginners/`

- Matplotlib ile görselleştirme
- Seaborn ile gelişmiş grafikler
- SciPy ile bilimsel hesaplamalar
- Scikit-learn ile preprocessing
- Eksik veri doldurma teknikleri

**Öğrenme Hedefleri:**
- ✅ Veri görselleştirme yapabilme
- ✅ EDA (Exploratory Data Analysis) sürecini uygulayabilme
- ✅ Eksik verileri doldurma yöntemlerini bilme
- ✅ Scikit-learn ile veri ön işleme yapabilme

### 📙 Seviye 3: Makine Öğrenmesi (Detaylı)

**Klasör:** `03_machine_learning/`

**Sınıflandırma Algoritmaları:**
- Logistic Regression
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)
- Decision Trees
- Naive Bayes

**Regresyon Algoritmaları:**
- Linear Regression (Ridge, Lasso, Elastic Net)
- Polynomial Regression

**Ensemble Methods:**
- Random Forest
- Gradient Boosting (XGBoost, LightGBM)
- Voting, Stacking, Blending

**Unsupervised Learning:**
- K-Means Clustering
- Hierarchical Clustering
- DBSCAN

**Model Değerlendirme:**
- Classification & Regression metrikleri
- Cross-validation teknikleri
- ROC-AUC, Confusion Matrix
- Learning curves

**Feature Engineering:**
- Feature selection
- Feature scaling
- Encoding techniques
- Feature creation

**Model Optimizasyonu:**
- Hyperparameter tuning (Grid Search, Random Search, Bayesian Optimization)
- Optuna, Hyperopt

**Gerçek Projeler:**
- ML Article Project (hava kirliliği, öğrenci başarısı, hava durumu)
- Preprocessing from scratch

**Öğrenme Hedefleri:**
- ✅ Temel ve ileri seviye ML algoritmalarını anlama ve uygulama
- ✅ Model performansını detaylı bir şekilde değerlendirme
- ✅ Feature engineering tekniklerini uygulama
- ✅ Hyperparameter tuning yapabilme
- ✅ Ensemble methods kullanabilme
- ✅ Gerçek veri setleri ile kapsamlı projeler yapabilme

## 📊 Proje Örnekleri

Bu repo içinde şu gerçek projeler bulunmaktadır:

1. **NBA Oyuncu Analizi** (`01_numpy_pandas/notebooks/NBA Players .ipynb`)
   - Gerçek NBA verileri ile istatistiksel analiz

2. **Eksik Veri Doldurma Projesi** (`02_data_analysis_for_beginners/missing_data_imputation/`)
   - Farklı imputation yöntemlerinin karşılaştırılması

3. **ML Article Projesi** (`03_machine_learning/ml_article_project/`)
   - Hava kirliliği, öğrenci başarısı ve hava durumu veri setleri
   - KNN, Naive Bayes, Decision Tree algoritmaları
   - SMOTE ile dengesiz veri setlerini dengeleme

## 🛠️ Kullanılan Teknolojiler

- **NumPy** - Sayısal hesaplamalar
- **Pandas** - Veri manipülasyonu
- **Matplotlib** - Veri görselleştirme
- **Seaborn** - İstatistiksel görselleştirme
- **SciPy** - Bilimsel hesaplamalar
- **Scikit-learn** - Makine öğrenmesi
- **Jupyter Notebook** - Etkileşimli geliştirme

## 📚 Ek Kaynaklar

- [NumPy Resmi Dokümantasyon](https://numpy.org/doc/)
- [Pandas Resmi Dokümantasyon](https://pandas.pydata.org/docs/)
- [Scikit-learn Kullanıcı Kılavuzu](https://scikit-learn.org/stable/user_guide.html)
- [Matplotlib Galeri](https://matplotlib.org/stable/gallery/index.html)

## 🤝 Katkıda Bulunma

Bu projeye katkıda bulunmak için:

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit edin (`git commit -m 'Add some amazing feature'`)
4. Push edin (`git push origin feature/amazing-feature`)
5. Pull Request açın

## 📝 Lisans

Bu proje eğitim amaçlı hazırlanmıştır.

## 👤 Yazar

**Sevgi Nur Kara**

- GitHub: [@SevgiNurKARA](https://github.com/SevgiNurKARA)

## 🙏 Teşekkürler

Bu öğrenme yolunu takip eden herkese başarılar dilerim! Sorularınız için issue açabilirsiniz.

---

⭐ Bu repo'yu beğendiyseniz yıldız vermeyi unutmayın!

