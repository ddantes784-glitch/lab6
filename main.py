list = [6, 7, 8, 9, 4, 4, 2]
k = 3
# Сдвиг влево
left = list[k:] + list[:k]
print(f'Сдвиг  влево: {left}')
# Сдвиг вправо
right = list[-k:] + list[:-k]
print(f'Сдвиг  вправо: {right}')