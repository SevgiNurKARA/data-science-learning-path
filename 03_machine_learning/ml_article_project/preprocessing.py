import os
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import KBinsDiscretizer

# Veri setleri dizini
input_folder = "completed_data"
output_folder = "output_folder"

# Tüm veri setlerini işleme
for filename in os.listdir(input_folder):
    if filename.endswith(".csv"):
        # Veri setini yükle
        data = pd.read_csv(os.path.join(input_folder, filename))
        
        # Sınıf etiketini son sütun olarak ayarla
        X = data.iloc[:, :-1]  # Tüm sütunlar hariç son sütun
        y = data.iloc[:, -1]   # Son sütun (sınıf etiketi)
        
        # 1. Discretization (Naive Bayes için)
        discretizer = KBinsDiscretizer(n_bins=5, encode='ordinal', strategy='uniform')
        X_discretized = discretizer.fit_transform(X)
        discretized_data = pd.DataFrame(X_discretized, columns=X.columns)
        discretized_data['target'] = y  # Hedef etiketini tekrar ekle
        
        discretized_filename = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_discretized.csv")
        discretized_data.to_csv(discretized_filename, index=False)
        
        # 2. Normalization (kNN için)
        scaler = MinMaxScaler()
        X_normalized = scaler.fit_transform(X)
        normalized_data = pd.DataFrame(X_normalized, columns=X.columns)
        normalized_data['target'] = y  # Hedef etiketini tekrar ekle
        
        normalized_filename = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_normalized.csv")
        normalized_data.to_csv(normalized_filename, index=False)

        # Ham veri kaydedilebilir, gerekirse uncomment edebilirsiniz
        # raw_filename = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_raw.csv")
        # data.to_csv(raw_filename, index=False)
