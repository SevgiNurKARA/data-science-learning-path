import random

# Dosya İşlemleri
def read_data_from_txt(file_path):
    """ Txt dosyasından veriyi oku ve liste olarak döndür """
    with open(file_path, 'r') as file:
        return [line.strip().split(',') for line in file.readlines()]

def write_data_to_txt(file_path, data):
    """ Veriyi txt dosyasına yaz """
    with open(file_path, 'w') as file:
        for row in data:
            file.write(','.join(map(str, row)) + '\n')

def write_results_to_txt(file_path, centroids, assignments, data):
    """ K-Means sonuçlarını txt dosyasına yazdır """
    with open(file_path, 'w') as file:
        file.write("Küme Merkezleri:\n")
        for i, centroid in enumerate(centroids):
            file.write(f"Küme {i} Merkezi: {', '.join(map(str, centroid))}\n")

        file.write("\nAtamalar:\n")
        for i, assignment in enumerate(assignments):
            file.write(f"Veri Noktası {i} -> Küme {assignment}\n")

        file.write("\nGüncellenmiş Veri:\n")
        for row in data:
            file.write(','.join(map(str, row)) + '\n')

# Veri Temizleme ve Hazırlama
def clean_data(data):
    """ '?' karakteri içeren satırları çıkar """
    return [row for row in data if '?' not in row]

def find_classes(data):
    """ Verideki sınıfları bul ve döndür """
    return list(set(row[-1] for row in data))

def calculate_means(data, classes):
    """ Her sınıf ve özellik için ortalamaları hesapla """
    num_columns = len(data[0]) - 1
    means = [[0] * num_columns for _ in range(len(classes))]
    
    for i, class_label in enumerate(classes):
        for col in range(num_columns):
            values = [float(row[col]) for row in data if row[col] != '?' and row[-1] == class_label]
            means[i][col] = sum(values) / len(values) if values else 0
    return means

def fill_missing_values(data, means, classes):
    """ Kayıp '?' değerlerini ortalamalarla doldur """
    num_columns = len(data[0]) - 1
    
    for row in data:
        for col in range(num_columns):
            if row[col] == '?':
                class_index = classes.index(row[-1])
                row[col] = means[class_index][col]
    
    return data

# Oversampling
def random_oversampling(data):
    """ Azınlık sınıflarını rastgele örnekleme ile dengeler """
    class_counts = {label: 0 for label in find_classes(data)}
    
    for row in data:
        class_counts[row[-1]] += 1

    max_count = max(class_counts.values())
    oversampled_data = data.copy()

    for class_label, count in class_counts.items():
        if count < max_count:
            class_samples = [row for row in data if row[-1] == class_label]
            oversampled_data.extend(random.choices(class_samples, k=max_count - count))
    
    return oversampled_data

# K-Means Algoritması
def kmeans_clustering(data, K=4, max_iter=1000):
    """ K-Means kümeleme algoritmasını uygular """
    num_rows = len(data)
    num_cols = len(data[0]) - 1

    # K için geçerli aralık kontrolü
    if K <= 0:
        raise ValueError("K negatif olamaz veya sıfır olamaz.")
    if K > num_rows:
        raise ValueError(f"K değeri, veri sayısından fazla olamaz. (Veri sayısı: {num_rows}, K: {K})")

    # Rastgele merkezler seç
    centroids = [data[random.randint(0, num_rows - 1)][:-1] for _ in range(K)]

    for iteration in range(max_iter):
        # Mesafeleri hesapla
        distances = [[sum(abs(float(data[row][col]) - float(centroid[col])) for col in range(num_cols)) for centroid in centroids] for row in range(num_rows)]

        # Her veri noktası için en yakın merkezi ata
        assignments = [dist.index(min(dist)) for dist in distances]

        # Merkezleri güncelle
        new_centroids = [[0] * num_cols for _ in range(K)]
        counts = [0] * K
        
        for row, cluster in zip(data, assignments):
            for col in range(num_cols):
                new_centroids[cluster][col] += float(row[col])
            counts[cluster] += 1
        
        for i in range(K):
            if counts[i] > 0:
                new_centroids[i] = [x / counts[i] for x in new_centroids[i]]

        # Eğer merkezler değişmediyse dur
        if centroids == new_centroids:
            print(f"K-Means {iteration} iterasyonda sonlandı.")
            break
        
        centroids = new_centroids

    return data, centroids, assignments

# Ana Akış
def main():
    input_file_path = 'data.txt'
    output_file_path = 'output.txt'
    results_file_path = 'results.txt'

    # 1. Veriyi oku
    data = read_data_from_txt(input_file_path)

    # 2. Veriyi temizle
    data = clean_data(data)

    # 3. Sınıfları bul
    classes = find_classes(data)

    # 4. Eksik verileri doldur
    means = calculate_means(data, classes)
    data = fill_missing_values(data, means, classes)

    # 5. Oversampling uygula
    data = random_oversampling(data)

    # 6. K-Means kümeleme yap
    K = 4  # K'nin değeri burada ayarlanır
    data, centroids, assignments = kmeans_clustering(data, K)

    # 7. Güncellenen veriyi ve sonuçları dosyaya yaz
    write_data_to_txt(output_file_path, data)
    write_results_to_txt(results_file_path, centroids, assignments, data)

    print("Sonuçlar 'results.txt' dosyasına yazdırıldı.")

# Programı çalıştır
if __name__ == "__main__":
    main()
