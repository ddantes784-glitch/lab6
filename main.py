list = [6, 7, 8, 9, 4, 4, 2]
list.sort()
print(f"Отсортированный список: {list}")
# поиск длины и середины
l = len(list)
mid = l//2
# если длина списка равна четному, то выводим мид, если нет то выводим ср. ариф. двух центральных
if l % 2 != 0:
    median = list[mid]
else:
    median = (list[mid-1] + list[mid]) / 2
print(f"Медиана: {median}")
    
    