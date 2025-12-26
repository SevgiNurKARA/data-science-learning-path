def discretize_data(data, k):
    if k <= 0:
        raise ValueError("k must be a positive integer greater than 0.")
    if k > len(data):
        raise ValueError(f"k cannot be larger than the number of data points ({len(data)}).")
    
    data_sorted = sorted(data)
    
    n = len(data)
    interval = n // k
    
    bin_edges = [data_sorted[0]]
    for i in range(1, k):
        split_point = data_sorted[i * interval - 1]
        bin_edges.append(split_point)
    bin_edges.append(data_sorted[-1])
    
    discretized_data = []
    for value in data:
        for j in range(len(bin_edges) - 1):
            if bin_edges[j] <= value <= bin_edges[j + 1]:
                discretized_data.append(j + 1)  
                break
    
    return discretized_data, bin_edges

def read_data_from_file(input_file):
    with open(input_file, 'r') as file:
        # Veriyi dosyadan okuyup listeye çevir
        data = file.read().splitlines()
        data = list(map(int, data))  # Veriyi integer listeye çevir
    return data

def write_output_to_file(output_file, discretized_data, bin_edges):
    with open(output_file, 'w') as file:
        file.write("Discretized data: " + ', '.join(map(str, discretized_data)) + '\n')
        file.write("Bin edges: " + ', '.join(map(str, bin_edges)) + '\n')

# Örnek kullanım
input_file = 'input_data.txt'  # Veri bu dosyadan okunacak
output_file = 'output_data.txt'  # Sonuçlar bu dosyaya yazılacak
k = 3  # Kaç parçaya bölüneceği

# Adım 1: Veriyi dosyadan oku
data = read_data_from_file(input_file)

# Adım 2: Discretize işlemini uygula
try:
    discretized_data, bin_edges = discretize_data(data, k)
    # Adım 3: Sonuçları dosyaya yaz
    write_output_to_file(output_file, discretized_data, bin_edges)
except ValueError as e:
    print(f"Error: {e}")
