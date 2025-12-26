import os
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import numpy as np


# Veri setleri dizini
input_folder = "completed_data"  # Veri setlerinin bulunduğu klasör
output_folder = "result"   # Çıktıların kaydedileceği klasör


# Sonuçları saklayacak boş bir liste oluşturuyoruz
results = []

# Tüm veri setlerini işleme
for filename in os.listdir(input_folder):
    if filename.endswith(".csv"):  # Veri setinin CSV formatında olduğunu varsayıyoruz
        print(f"\nVeri Seti: {filename}")
        
        # Veri setini yükle
        data = pd.read_csv(os.path.join(input_folder, filename))
        
        # Hedef sütunu son sütun olarak al
        target_column = data.columns[-1]
        
        print(f"Hedef Sütun: {target_column}")
        
        # Özellikler (X) ve hedef değişkenini (y) ayır
        X = data.drop(target_column, axis=1)
        y = data[target_column]
        
        # Karar Ağacı modelini oluştur
        clf = DecisionTreeClassifier(random_state=42)
        
        # Çapraz doğrulama (Cross-validation) ile modelin doğruluğunu değerlendirin
        cv_scores = cross_val_score(clf, X, y, cv=5)  # 5 katlı çapraz doğrulama
        
        print(f"Çapraz doğrulama doğruluk oranları: {cv_scores}")
        print(f"Ortalama doğruluk oranı: {cv_scores.mean() * 100:.2f}%")
        
        # Modeli tüm veri ile eğitmek
        clf.fit(X, y)
        
        # Modelin doğruluğunu test et (eğitim verisi üzerinde)
        y_pred = clf.predict(X)
        
        # Metrikleri hesapla
        accuracy = accuracy_score(y, y_pred)
        precision = precision_score(y, y_pred, average='weighted')  # Weighted average
        recall = recall_score(y, y_pred, average='weighted')  # Weighted average
        f1 = f1_score(y, y_pred, average='weighted')  # Weighted average
        
        print(f"Modelin Doğruluk Oranı: {accuracy * 100:.2f}%")
        print(f"Precision: {precision:.2f}")
        print(f"Recall: {recall:.2f}")
        print(f"F1-Score: {f1:.2f}")
        
        # Sonuçları listeye ekle
        results.append({
            'Dataset': filename,
            'Mean CV Accuracy': cv_scores.mean() * 100,
            'Training Accuracy': accuracy * 100,
            'Precision': precision,
            'Recall': recall,
            'F1-Score': f1
        })

# Sonuçları DataFrame'e dönüştür
results_df = pd.DataFrame(results)

# Sonuçları CSV olarak kaydet
results_df.to_csv(os.path.join(output_folder, "decision_tree_metrics_results.csv"), index=False)

# Sonuçları ekrana yazdır
print("\nTüm Sonuçlar:")
print(results_df)
