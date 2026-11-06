students = [
    ('Кирилл', 18, 4.6),
    ('Вася', 17, 3.9),
    ('Валера', 25, 4.2),
    ('Петя', 20, 4.9)
]
# самый старший
oldest = max(students, key=lambda s: s[1])
print(f'Самый старший: {oldest[0]}, {oldest[1]} лет')
# с самым высоким баллом
best = max(students, key=lambda s: s[2])
print(f"Лучший студент: {best[0]}, балл {best[2]}")
# средний возраст
avg_age = sum(s[1] for s in students) / len(students)
print(f"Средний возраст: {avg_age:.1f}")
# сортировка по баллу (убывание)
sorted_students = sorted(students, key=lambda s: s[2], reverse=True)
print("\nПо баллу:")
for name, age, gpa in sorted_students:
    print(f"{name}: {gpa}")
