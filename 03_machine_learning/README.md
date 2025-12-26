# 📙 Seviye 3: Makine Öğrenmesi (Detaylı)

Bu seviye, makine öğrenmesi algoritmalarını, model değerlendirme tekniklerini, feature engineering'i ve gerçek projeleri kapsamlı bir şekilde kapsar.

## 🎯 Öğrenme Hedefleri

Bu seviyeyi tamamladıktan sonra:
- ✅ Temel ve ileri seviye ML algoritmalarını anlayabilirsiniz
- ✅ Veri ön işleme ve feature engineering tekniklerini uygulayabilirsiniz
- ✅ Model performansını detaylı bir şekilde değerlendirebilirsiniz
- ✅ Hyperparameter tuning yapabilirsiniz
- ✅ Ensemble methods kullanabilirsiniz
- ✅ Gerçek veri setleri ile kapsamlı projeler yapabilirsiniz
- ✅ Kütüphane kullanmadan preprocessing ve algoritmaları from scratch implement edebilirsiniz

## 📚 İçerik Yapısı

### 🔵 Sınıflandırma Algoritmaları

#### 📊 Logistic Regression
- Binary ve multiclass classification
- Sigmoid fonksiyonu ve decision boundary
- From scratch implementasyon
- **Klasör:** `logistic_regression/`

#### 🎯 Support Vector Machine (SVM)
- Maximum margin classifier
- Kernel tricks (Linear, Polynomial, RBF)
- Soft margin ve C parametresi
- **Klasör:** `svm/`

#### 🔍 K-Nearest Neighbors (KNN)
- Lazy learning algoritması
- Distance metrics (Euclidean, Manhattan)
- K değeri seçimi
- Classification ve Regression
- **Klasör:** `knn/`

#### 🌳 Decision Tree
- Karar ağaçları algoritması
- Gini impurity ve Entropy
- Pruning teknikleri
- **Klasör:** `decision_tree/`

#### 📊 Naive Bayes
- Bayes teoremi
- Gaussian, Multinomial, Bernoulli Naive Bayes
- **Klasör:** `naive_bayes/`

### 🟢 Regresyon Algoritmaları

#### 📈 Linear Regression
- Simple ve Multiple Linear Regression
- Polynomial Regression
- Ridge, Lasso, Elastic Net (Regularization)
- From scratch implementasyon
- **Klasör:** `linear_regression/`

### 🟡 Ensemble Methods

#### 🌲 Random Forest
- Bagging (Bootstrap Aggregating)
- Feature importance
- Out-of-bag scoring
- **Klasör:** `random_forest/`

#### 🚀 Gradient Boosting
- Boosting algoritması
- XGBoost, LightGBM, CatBoost
- Learning rate ve early stopping
- **Klasör:** `gradient_boosting/`

#### 🎭 Ensemble Methods
- Voting Classifier
- Stacking (Stacked Generalization)
- Blending
- **Klasör:** `ensemble_methods/`

### 🟣 Unsupervised Learning

#### 🎯 Clustering
- K-Means Clustering
- Hierarchical Clustering
- DBSCAN (Density-based)
- Clustering evaluation metrics
- **Klasör:** `clustering/`

### 🔧 Veri Ön İşleme & Feature Engineering

#### 🔧 Preprocessing From Scratch
Kütüphane kullanmadan veri ön işleme:
- Data Encoding
- Discretization
- Missing Value Handling
- Oversampling
- k-Means (from scratch)
- **Klasör:** `preprocessing_from_scratch/`

#### 🔧 Feature Engineering
- Feature Selection (Univariate, RFE, Feature Importance)
- Feature Scaling (Standardization, Normalization)
- Feature Creation (Polynomial, Interaction)
- Encoding Techniques (One-Hot, Label, Target)
- **Klasör:** `feature_engineering/`

### 📊 Model Değerlendirme

#### 📊 Model Evaluation
- **Classification Metrics:** Accuracy, Precision, Recall, F1-Score, Confusion Matrix, ROC-AUC
- **Regression Metrics:** MAE, MSE, RMSE, R²
- **Cross-Validation:** K-Fold, Stratified K-Fold, Leave-One-Out
- **Learning Curves:** Overfitting/Underfitting detection
- **Klasör:** `model_evaluation/`

### ⚙️ Model Optimizasyonu

#### ⚙️ Hyperparameter Tuning
- Grid Search CV
- Random Search CV
- Bayesian Optimization
- Optuna, Hyperopt
- **Klasör:** `hyperparameter_tuning/`

### 🚀 Gerçek Projeler

#### 🚀 ML Article Project
Kapsamlı makine öğrenmesi projesi:
- **Veri Setleri:** Hava Kirliliği, Öğrenci Başarısı, Hava Durumu
- **Eksik Veri Doldurma:** Mean, Mode, KNN, Multiple Imputation
- **Dengesiz Veri:** SMOTE
- **Algoritmalar:** KNN, Naive Bayes, Decision Tree
- **Performans Metrikleri:** MAE, MSE, Accuracy, Precision, Recall, F1-Score
- **Klasör:** `ml_article_project/`

## 🚀 Önerilen Öğrenme Yolu

### 1️⃣ Temel Algoritmalar (1-2 hafta)
1. **Linear Regression** (`linear_regression/`)
2. **Logistic Regression** (`logistic_regression/`)
3. **KNN** (`knn/`)
4. **Decision Tree** (`decision_tree/`)
5. **Naive Bayes** (`naive_bayes/`)

### 2️⃣ İleri Algoritmalar (1-2 hafta)
1. **SVM** (`svm/`)
2. **Random Forest** (`random_forest/`)
3. **Gradient Boosting** (`gradient_boosting/`)

### 3️⃣ Model Değerlendirme (1 hafta)
1. **Model Evaluation** (`model_evaluation/`)
   - Classification ve Regression metrikleri
   - Cross-validation
   - Learning curves

### 4️⃣ Feature Engineering (1 hafta)
1. **Feature Engineering** (`feature_engineering/`)
2. **Preprocessing From Scratch** (`preprocessing_from_scratch/`)

### 5️⃣ Model Optimizasyonu (1 hafta)
1. **Hyperparameter Tuning** (`hyperparameter_tuning/`)

### 6️⃣ Ensemble Methods (1 hafta)
1. **Ensemble Methods** (`ensemble_methods/`)

### 7️⃣ Unsupervised Learning (1 hafta)
1. **Clustering** (`clustering/`)

### 8️⃣ Gerçek Projeler (2-3 hafta)
1. **ML Article Project** (`ml_article_project/`)
2. Kendi projelerinizi geliştirin

## ✅ Detaylı Kontrol Listesi

### Temel Algoritmalar
- [ ] Linear Regression notebook'u tamamlandı
- [ ] Logistic Regression notebook'u tamamlandı
- [ ] KNN notebook'u tamamlandı
- [ ] Decision Tree notebook'u tamamlandı
- [ ] Naive Bayes notebook'u tamamlandı

### İleri Algoritmalar
- [ ] SVM notebook'u tamamlandı
- [ ] Random Forest notebook'u tamamlandı
- [ ] Gradient Boosting notebook'u tamamlandı

### Model Değerlendirme
- [ ] Classification metrikleri öğrenildi
- [ ] Regression metrikleri öğrenildi
- [ ] Confusion matrix yorumlandı
- [ ] ROC-AUC analizi yapıldı
- [ ] Cross-validation uygulandı
- [ ] Learning curves çizildi

### Feature Engineering
- [ ] Feature selection teknikleri uygulandı
- [ ] Feature scaling yapıldı
- [ ] Yeni feature'lar oluşturuldu
- [ ] Encoding teknikleri öğrenildi
- [ ] Preprocessing from scratch teknikleri anlaşıldı

### Model Optimizasyonu
- [ ] Grid Search uygulandı
- [ ] Random Search uygulandı
- [ ] Bayesian Optimization öğrenildi
- [ ] Optuna ile tuning yapıldı

### Ensemble Methods
- [ ] Voting Classifier kullanıldı
- [ ] Stacking uygulandı
- [ ] Blending yapıldı

### Unsupervised Learning
- [ ] K-Means clustering uygulandı
- [ ] Hierarchical clustering yapıldı
- [ ] DBSCAN öğrenildi
- [ ] Clustering evaluation metrikleri kullanıldı

### Projeler
- [ ] ML Article projesi tamamlandı
- [ ] Kendi veri setimle proje yapıldı
- [ ] Farklı algoritmalar karşılaştırıldı
- [ ] Model performansları analiz edildi

## 📊 Proje Önerileri

### Başlangıç Seviyesi
1. **Titanic Dataset** - Binary classification
2. **House Prices** - Regression
3. **Iris Dataset** - Multiclass classification

### Orta Seviye
1. **Customer Churn Prediction** - Imbalanced dataset
2. **Credit Card Fraud Detection** - Anomaly detection
3. **Sales Forecasting** - Time series regression

### İleri Seviye
1. **Kaggle Competitions** - Gerçek dünya problemleri
2. **End-to-End ML Pipeline** - Veri toplama, preprocessing, modeling, deployment
3. **Multi-class Multi-label Classification**

## 🎓 İleri Seviye Konular

- Model Interpretability (SHAP, LIME)
- AutoML
- Neural Networks (Deep Learning'e geçiş)
- Time Series Analysis
- Recommendation Systems
- Natural Language Processing

## 🔗 Sonraki Adımlar

Bu seviyeyi tamamladıktan sonra:
- **Seviye 4: Deep Learning** - Neural networks, CNN, RNN
- **Seviye 5: Advanced ML & Deployment** - Model deployment, MLOps
- **Kaggle Competitions** - Gerçek dünya problemleri
- **Portfolio Projects** - Kendi projelerinizi geliştirin

## 📚 Ek Kaynaklar

- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [Machine Learning Mastery](https://machinelearningmastery.com/)
- [Kaggle Learn](https://www.kaggle.com/learn)
- [Fast.ai](https://www.fast.ai/)

---

**Tebrikler!** 🎉 Makine öğrenmesi yolculuğunuzda önemli bir adım attınız!
