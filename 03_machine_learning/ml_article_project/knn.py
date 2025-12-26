import os
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
import seaborn as sns

input_folder = "knn"
output_folder = "output_folder"

def evaluate_knn(input_folder):
    results = []

    for filename in os.listdir(input_folder):
        if filename.endswith(".csv"):
            print(f"\nProcessing {filename}...")
            data = pd.read_csv(os.path.join(input_folder, filename))
            
            target = data.iloc[:, -1]
            features = data.iloc[:, :-1]
            
            X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

            knn = KNeighborsClassifier(n_neighbors=5)
            knn.fit(X_train, y_train)

            y_pred = knn.predict(X_test)

            accuracy = accuracy_score(y_test, y_pred)
            precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
            recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
            f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)
            
            cv_accuracy = np.mean(cross_val_score(knn, features, target, cv=5, scoring='accuracy'))
            
            results.append({
                'Dataset': filename,
                'Mean CV Accuracy': cv_accuracy * 100,
                'Training Accuracy': accuracy * 100,
                'Precision': precision,
                'Recall': recall,
                'F1-Score': f1
            })

    return results

results = evaluate_knn(input_folder)

results_df = pd.DataFrame(results)

print("\nKNN Model Performans Sonuçları:")
print(results_df)

results_df.to_csv(os.path.join(output_folder, "knn_performance.csv"), index=False)

plt.figure(figsize=(10, 6))
sns.barplot(x='Dataset', y='Mean CV Accuracy', data=results_df, palette='viridis')
plt.xticks(rotation=90)
plt.title('KNN Mean CV Accuracy for Different Datasets')
plt.tight_layout()
plt.show()
