"""
Задание 3:
Запросить у пользователя 10 чисел и записать их в список A
Запросить у пользователя число N
Вывести пользователю сколько в списке A повторяется число N
"""

A = []
for i in range(10):
    numbers = int(input(f"Enter your numbers #{i}: "))
    A.append(numbers)
print(A)
N = int(input("Enter number N: "))
print(A.count(N))

print("End")
