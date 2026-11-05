import random

n = int(input("Введите N: "))
numbers = [random.randint(1, 100) for _ in range(n)]
print(f"Исходный список: {numbers}")
print(f"Сумма: {sum(numbers)}")
print(f"Среднее: {sum(numbers) / len(numbers):.2f}")
print(f"Минимум: {min(numbers)}")
print(f"Максимум: {max(numbers)}")
# Сортировка списка
numbers.sort()
print(f"Отсортированный: {numbers}")
# Удаление дубликатов из списка с сохранением порядка
unique = list(dict.fromkeys(numbers))
print(f"Без дубликатов: {unique}")
