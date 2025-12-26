import os
import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

input_folder = "completed_data"
output_folder = "result"

def load_and_process_data(input_folder, run_id):
    results = []
    confusion_matrices = {}

    for filename in os.listdir(input_folder):
        if filename.endswith(".csv"):
            print(f"\nProcessing {filename} (Run {run_id})...")
            data = pd.read_csv(os.path.join(input_folder, filename))
            
            target = data.iloc[:, -1]
            features = data.iloc[:, :-1]
            
            X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

            nb = GaussianNB()
            nb.fit(X_train, y_train)

            y_pred = nb.predict(X_test)

            accuracy = accuracy_score(y_test, y_pred)
            precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
            recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
            f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)
            
            cv_accuracy = np.mean(cross_val_score(nb, features, target, cv=5, scoring='accuracy'))

            cm = confusion_matrix(y_test, y_pred)
            confusion_matrices[f"{filename}_run_{run_id}"] = cm

            results.append({
                'Run': run_id,
                'Dataset': filename,
                'Mean CV Accuracy': cv_accuracy * 100,
                'Training Accuracy': accuracy * 100,
                'Precision': precision,
                'Recall': recall,
                'F1-Score': f1
            })

    return results, confusion_matrices

all_results = []
all_confusion_matrices = {}

for run_id in range(1, 11):  # 10 kez çalıştır
    run_results, run_confusion_matrices = load_and_process_data(input_folder, run_id)
    all_results.extend(run_results)
    all_confusion_matrices.update(run_confusion_matrices)


results_df = pd.DataFrame(all_results)
detailed_metrics = results_df.pivot_table(
    index='Run',
    values=['Mean CV Accuracy', 'Training Accuracy', 'Precision', 'Recall', 'F1-Score'],
    aggfunc='mean'
).reset_index()

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
results_df.to_csv(os.path.join(output_folder, "the_best_resultance_10_runs.csv"), index=False)
melted_results = detailed_metrics.melt(id_vars='Run', var_name='Metric', value_name='Value')

plt.figure(figsize=(10, 6))
for metric in ['Mean CV Accuracy', 'Training Accuracy', 'Precision', 'Recall', 'F1-Score']:
    plt.plot(detailed_metrics['Run'], detailed_metrics[metric], marker='o', label=metric)

plt.title("Performance Metrics Across 10 Runs")
plt.xlabel("Run")
plt.ylabel("Metric Value")
plt.legend(title="Metrics")
plt.grid()
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "performance_across_runs.png"))
plt.show()

