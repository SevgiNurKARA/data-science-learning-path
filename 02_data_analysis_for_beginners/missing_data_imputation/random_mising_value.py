#Gerekli kütüphaneleri import ediyoruz
import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
import numpy as np

#Veri setini okuyoruz
data=pd.read_csv("pcos_dataset.csv")

#Hedef değişkeni ve bağımsız değişkenleri belirliyoruz
X= data[['Age','BMI','Menstrual_Irregularity','Testosterone_Level(ng/dL)','Antral_Follicle_Count']]
Y= data['PCOS_Diagnosis']

#Veri setini eğitim ve test setlerine bölüyoruz
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

#SMOTE ile çoğaltma yapıyoruz
sm = SMOTE(random_state = 2)
X_train_res, y_train_res = sm.fit_resample(X_train, y_train)

# Rastgele eksik değerler oluşturma
missing_percentage = 0.05  
n_missing = int(missing_percentage * X_train_res.size)

# Rastgele indeksler seçme
missing_indices = (np.random.randint(0, X_train_res.shape[0], n_missing), 
                    np.random.randint(0, X_train_res.shape[1], n_missing))

# Eksik değerleri atama
X_train_res.iloc[missing_indices] = np.nan

# X ve Y'yi birleştirme
data_resampled = X_train_res.copy()
data_resampled['PCOS_Diagnosis'] = y_train_res

# Veriyi CSV olarak kaydetme
data_resampled.to_csv("data_resampled.csv", index=False)
