def read_data_from_txt(file_path):
    """ Veriyi txt dosyasından oku ve liste olarak geri döndür """
    with open(file_path, 'r') as file:
        lines = file.readlines()
    data = [line.strip().split(',') for line in lines]
    return data

def write_data_to_txt(file_path, data):
    """ Veriyi txt dosyasına yaz """
    with open(file_path, 'w') as file:
        for row in data:
            file.write(','.join(map(str, row)) + '\n')

def write_results_to_txt(file_path, centroids, assignments, data):
    """ K-Means sonuçlarını txt dosyasına yazdırır """
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

def clean_data(array2D):
    """ Verilerden '?' olanları çıkarır """
    return [row for row in array2D if row[-1] != '?']

def find_classes(array2D):
    """ Verideki sınıfları bulur """
    arraypassenger = []
    for row in array2D:
        if row[-1] not in arraypassenger:
            arraypassenger.append(row[-1])
    return arraypassenger

def calculate_means(array2D, arraypassenger):
    """ Her sınıf ve sütun için ortalama hesapla """
    arrayCol = len(array2D[0])
    tempmean = [[0 for _ in range(arrayCol - 1)] for _ in range(len(arraypassenger))]
    
    for e, passenger_class in enumerate(arraypassenger):
        for c in range(arrayCol - 1):
            sum_ = 0
            counter = 0
            for row in array2D:
                if row[c] != '?' and row[-1] == passenger_class:
                    sum_ += float(row[c])
                    counter += 1
            if counter > 0:
                tempmean[e][c] = sum_ / counter
    return tempmean

def fill_missing_values(array2D, tempmean, arraypassenger):
    """ Kayıp değerleri ortalama ile doldur """
    for a, row in enumerate(array2D):
        for b, value in enumerate(row[:-1]):
            if value == '?':
                for d, passenger_class in enumerate(arraypassenger):
                    if row[-1] == passenger_class:
                        array2D[a][b] = tempmean[d][b]
    return array2D

def kmeans_clustering(array2D, K=4, max_iter=1000):
    """ K-Means algoritmasını uygular """
    arrayRow = len(array2D)
    arrayCol = len(array2D[0])
    import random

    # Rastgele merkezler seç
    clusterCenter = [array2D[random.randint(0, arrayRow - 1)][:-1] for _ in range(K)]
    clusterDistance = [[0 for _ in range(K)] for _ in range(arrayRow)]
    centerCommitment = [0 for _ in range(arrayRow)]
    centerCommitmentpast = [0 for _ in range(arrayRow)]

    for iteration in range(max_iter):
        # Mesafelerin hesaplanması
        for m in range(K):
            for o in range(arrayRow):
                clusterDistance[o][m] = sum(abs(float(array2D[o][p]) - float(clusterCenter[m][p])) for p in range(arrayCol - 1))

        # Önceki atamalar kaydedilir
        centerCommitmentpast = centerCommitment[:]

        # En yakın merkezleri bulma
        for e in range(arrayRow):
            centerCommitment[e] = clusterDistance[e].index(min(clusterDistance[e]))

        # Atamalar değişmezse dur
        if centerCommitment == centerCommitmentpast:
            print("Son merkezler:", clusterCenter)
            print("Son atamalar:", centerCommitment)
            print(f"Kaç iterasyon sürdü: {iteration}")
            break

        # Merkezlerin güncellenmesi
        for m in range(K):
            for o in range(arrayCol - 1):
                summean = 0
                counter = 0
                for p in range(arrayRow):
                    if centerCommitment[p] == m:
                        summean += float(array2D[p][o])
                        counter += 1
                if counter > 0:
                    clusterCenter[m][o] = summean / counter

    return array2D, clusterCenter, centerCommitment

# Veri dosyasını oku
input_file_path = 'data.txt'
output_file_path = 'output.txt'
results_file_path = 'results.txt'
array2D = read_data_from_txt(input_file_path)

# Boş değerleri temizle
array2D = clean_data(array2D)

# Verideki sınıfları bul
arraypassenger = find_classes(array2D)

# Ortalama hesapla ve kayıp verileri doldur
tempmean = calculate_means(array2D, arraypassenger)
array2D = fill_missing_values(array2D, tempmean, arraypassenger)

# K-Means kümeleme
array2D, clusterCenter, centerCommitment = kmeans_clustering(array2D)

# Sonuçları output.txt dosyasına yazdır
write_data_to_txt(output_file_path, array2D)

# Sonuçları ayrı bir dosyaya yazdır (küme merkezleri, atamalar ve güncellenmiş veri)
write_results_to_txt(results_file_path, clusterCenter, centerCommitment, array2D)

print("Sonuçlar 'results.txt' dosyasına yazdırıldı.")
