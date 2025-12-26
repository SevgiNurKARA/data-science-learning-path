dizi = []

with open('data.txt', 'r') as file:
    lines = [line.strip() for line in file]

array2D = [line.split(',') for line in lines]

arrayCol = len(array2D[0])
arrayRow = len(array2D)

for j in range(arrayCol - 1):
    if not array2D[0][j].isdigit():
        for k in range(arrayRow):
            if array2D[k][j] not in dizi:
                dizi.append(array2D[k][j])
        for i in range(arrayRow):
            array2D[i][j] = dizi.index(array2D[i][j]) + 1
        dizi = []

for l in range(arrayRow):
    if array2D[l][arrayCol - 1] not in dizi:
        dizi.append(array2D[l][arrayCol - 1])

newarray = [[0 for _ in range(arrayCol + len(dizi) - 1)] for _ in range(arrayRow)]

for a in range(arrayRow):
    for b in range(arrayCol - 1):
        newarray[a][b] = array2D[a][b]

for c in range(len(dizi)):
    for d in range(arrayRow):
        if array2D[d][arrayCol - 1] == dizi[c]:
            newarray[d][arrayCol - 1 + c] = 1
        else:
            newarray[d][arrayCol - 1 + c] = 0

with open('output.txt', 'w') as output_file:
    for row in newarray:
        output_file.write(','.join(map(str, row)) + '\n')
