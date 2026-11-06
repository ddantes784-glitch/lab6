list1 = [12, 23, 34, 45, 56]
list2 = [45, 56, 67, 78, 89]
# Добавляем множества
set1 = set(list1)
set2 = set(list2)
union = set1 | set2
intersection = set1 & set2
difference = set1 - set2
print(f'Обьединение: {sorted(union)}')
print(f'пересечения: {sorted(intersection)}')
print(f'Разность: {sorted(difference)}')