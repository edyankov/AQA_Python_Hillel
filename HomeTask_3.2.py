"""Пользователь вводит с клавиатуры три числа в переменные a, b, c.
Найдите наибольшее число из них и запишите в переменную max.
"""

a = int(input("Enter number a:"))
b = int(input("Enter number b:"))
c = int(input("Enter number c:"))
max = 0

if a > b and a > c:
    max = a
elif b > c:
    max = b
else:
    max = c
print("Largest number:", max)

print("End")
