"""
Пользователь вводит с клавиатуры три числа в переменные a, b, c.
Если все числа больше 10 и первые два числа делятся на 3, то вывести yes, иначе no.
"""

a = int(input("Enter number a:"))
b = int(input("Enter number b:"))
c = int(input("Enter number c:"))
if a > 10 and a % 3 == 0:
    if b > 10 and b % 3 == 0:
        if c > 10:
            print("Yes")
else:
    print("No")

print("End")
