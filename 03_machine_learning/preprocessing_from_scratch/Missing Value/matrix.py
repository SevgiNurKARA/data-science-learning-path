def confusion_matrix_multi_class(y_true, y_pred):
    # Sınıfları belirle
    classes = sorted(set(y_true + y_pred))
    n_classes = len(classes)
    
    # Confusion matrix oluştur (NxN boyutunda, başlangıçta 0)
    confusion_matrix = [[0] * n_classes for _ in range(n_classes)]
    
    # Confusion matrix'i doldur
    for true, pred in zip(y_true, y_pred):
        true_idx = classes.index(true)  # Gerçek sınıfın indeksi
        pred_idx = classes.index(pred)  # Tahmin sınıfının indeksi
        confusion_matrix[true_idx][pred_idx] += 1
    
    return confusion_matrix, classes

def calculate_metrics_from_matrix(confusion_matrix, classes):
    # Sınıf bazlı metrikleri hesapla
    class_metrics = {}
    n_classes = len(classes)
    
    for i, cls in enumerate(classes):
        TP = confusion_matrix[i][i]
        FP = sum(confusion_matrix[j][i] for j in range(n_classes) if j != i)
        FN = sum(confusion_matrix[i][j] for j in range(n_classes) if j != i)
        TN = sum(
            confusion_matrix[j][k]
            for j in range(n_classes)
            for k in range(n_classes)
            if j != i and k != i
        )
        
        # Metrikleri hesapla
        sensitivity = TP / (TP + FN) if (TP + FN) > 0 else 0
        specificity = TN / (TN + FP) if (TN + FP) > 0 else 0
        precision = TP / (TP + FP) if (TP + FP) > 0 else 0
        npv = TN / (TN + FN) if (TN + FN) > 0 else 0
        accuracy = (TP + TN) / (TP + TN + FP + FN) if (TP + TN + FP + FN) > 0 else 0
        
        class_metrics[cls] = {
            "Sensitivity (Recall)": sensitivity,
            "Specificity": specificity,
            "Precision": precision,
            "Negative Predictive Value (NPV)": npv,
            "Accuracy": accuracy,
        }
    
    # Makro Ortalama Hesapla
    avg_metrics = {
        "Sensitivity (Recall)": sum(m["Sensitivity (Recall)"] for m in class_metrics.values()) / n_classes,
        "Specificity": sum(m["Specificity"] for m in class_metrics.values()) / n_classes,
        "Precision": sum(m["Precision"] for m in class_metrics.values()) / n_classes,
        "Negative Predictive Value (NPV)": sum(m["Negative Predictive Value (NPV)"] for m in class_metrics.values()) / n_classes,
        "Accuracy": sum(m["Accuracy"] for m in class_metrics.values()) / n_classes,
    }
    
    return class_metrics, avg_metrics

# Örnek veri
y_true = [1, 0, 2, 1, 0, 2, 1, 2, 0, 1]
y_pred = [1, 0, 1, 1, 0, 2, 2, 2, 0, 1]

# Confusion matrix oluştur ve sınıfları belirle
confusion_matrix, classes = confusion_matrix_multi_class(y_true, y_pred)

# Confusion matrix'i yazdır
print("Confusion Matrix:")
for row in confusion_matrix:
    print(row)

# Metrikleri hesapla
class_metrics, avg_metrics = calculate_metrics_from_matrix(confusion_matrix, classes)

# Sonuçları yazdır
print("\nSınıf Bazlı Metrikler:")
for cls, metrics in class_metrics.items():
    print(f"\nClass {cls}:")
    for metric, value in metrics.items():
        print(f"  {metric}: {value:.2f}")

print("\nMakro Ortalama Metrikler:")
for metric, value in avg_metrics.items():
    print(f"{metric}: {value:.2f}")
