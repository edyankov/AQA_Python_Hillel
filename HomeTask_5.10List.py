"""
Задание 5:
Запросить у пользователя 5 чисел и записать их в список A
Записать все числа из списка A которые больше 5 в список C
"""

A = []
C = []
for i in range(5):
    numbers = int(input(f"Enter your numbers #{i}: "))
    A.append(numbers)
print("List A: ", A)

C = [i for i in A if i > 5]
print("List C: ", C)

print("End")
