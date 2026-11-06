m1 = [
    [1, 2],
    [3, 4]
]
m2 = [
    [5, 6],
    [7, 8]
]
resadd = [
    [0, 0],
    [0, 0]
]
for i in range(2):
    for j in range(2):
        resadd[i][j] = m1[i][j] + m2[i][j]
print("Сложение:")
for row in resadd:
    print(row)
resvi = [
    [0, 0],
    [0, 0]
]
for i in range(2):
    for j in range(2):
        resvi[i][j] = m1[i][j] - m2[i][j]
print("\nВычитание:")
for row in resvi:
    print(row)
resum = [
    [0, 0],
    [0, 0]
]
for i in range(2):
    for j in range(2):
        for k in range(2):
            resum[i][j] += m1[i][k] * m2[k][j]
print("\nУмножение:")
for row in resum:
    print(row)