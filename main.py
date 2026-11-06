matrix = [
    [1, 2, 3],
    [3, 6, 9],
    [6, 12, 18]
]
# unpacking with zip
transposed = [list(row) for row in zip(*matrix)]
# outpoot
print('Исходная матрица: ')
for row in matrix:
    print(row)
print('Транспонированная матрица: ')
for row in transposed:
    print(row)
