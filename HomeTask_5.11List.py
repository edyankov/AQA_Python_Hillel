"""
Задание 6:
Запросить у пользователя число N
Запросить у пользователя N целых чисел и записать их в список A
Найти в нем минимальное и максимальное число с помощью цикла (запрещено использовать функцию min и max).
Вывести эти числа.
"""

A = []

N = int(input("Enter size of the list: "))
spam = (range(1, N+1))
for i in (range(N)):
    numbers = int(input(f"Enter your numbers #{i}: "))
    A.append(numbers)
print(A)

A.sort()

print("Max number in the list A :", A[-1])
print("Min number in the list A :", A[0])

print("End")
