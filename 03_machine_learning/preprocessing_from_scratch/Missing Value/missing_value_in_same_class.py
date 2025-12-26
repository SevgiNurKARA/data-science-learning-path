# Veriyi dosyadan oku
def read_data(filename):
    with open(filename, 'r') as file:
        return [line.strip().split(',') for line in file]

# Geçerli sayısal değer olup olmadığını kontrol eden bir fonksiyon
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# String değerleri sayısal değerlere dönüştür
def convert_to_float(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != '?' and is_float(data[i][j]):
                data[i][j] = float(data[i][j])
    return data

# Sınıf bazlı ortalama hesapla
def calculate_class_means(data):
    class_means = {}
    for row in data:
        class_label = row[-1]  # Son sütun sınıf etiketi
        if class_label not in class_means:
            class_means[class_label] = [[] for _ in range(len(row) - 1)]
        
        for i, value in enumerate(row[:-1]):
            if isinstance(value, float):
                class_means[class_label][i].append(value)
    
    # Ortalamaları hesapla
    for class_label in class_means:
        for i in range(len(class_means[class_label])):
            if class_means[class_label][i]:
                class_means[class_label][i] = sum(class_means[class_label][i]) / len(class_means[class_label][i])
            else:
                class_means[class_label][i] = None
    
    return class_means

# Eksik değerleri sınıf bazlı ortalama ile doldur
def impute_missing_values(data, class_means):
    for row in data:
        class_label = row[-1]
        for i in range(len(row) - 1):
            if row[i] == '?':
                if class_means[class_label][i] is not None:
                    row[i] = class_means[class_label][i]
                else:
                    # Eğer o sınıf için ortalama yoksa, tüm sınıfların ortalamasını kullan
                    all_values = [means[i] for means in class_means.values() if means[i] is not None]
                    if all_values:
                        row[i] = sum(all_values) / len(all_values)
                    else:
                        row[i] = 0  # Hiçbir ortalama bulunamazsa 0 kullan
    return data

# Sonuçları dosyaya yaz
def write_results(filename, data):
    with open(filename, 'w') as output_file:
        for row in data:
            output_file.write(','.join(map(str, row)) + '\n')

# Ana işlem
def process_data(input_file, output_file):
    data = read_data(input_file)
    data = convert_to_float(data)
    class_means = calculate_class_means(data)
    data = impute_missing_values(data, class_means)
    write_results(output_file, data)
    print(f"İşlem tamamlandı. Sonuçlar '{output_file}' dosyasına kaydedildi.")

# Kodu çalıştır
process_data('p2_data.txt', 'p2_output.txt')