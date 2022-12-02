"""
Задание 4:
Запросить у пользователя число N
Запросить у пользователя N чисел и записать их в список A
Вывести список в обратной последовательности
"""

A = []
N = int(input("Enter size of the list: "))
spam = (range(1, N+1))
for i in (range(N)):
    numbers = int(input(f"Enter your numbers #{i}: "))
    A.append(numbers)
print(A)

print(list(reversed(A)))

print("End")
