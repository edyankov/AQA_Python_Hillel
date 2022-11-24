"""
Задание со звездочкой:
Вывести треугольник #3 с шириной N с помощью цикла for
"""

n = int(input("Enter the width of the triangle:"))
for i in range(n):
    print(" " * i + "*" * (n-i))

print('Triangle is drawn')
