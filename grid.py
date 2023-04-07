n = 100
matrix = []
i = 0

for _ in range(n):
    row = []
    for _ in range(n):
        row.append(i)
        i += 1
    matrix.append(row)

print(matrix)