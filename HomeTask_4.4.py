"""
Задание со звездочкой:
Вывести треугольник #4 с шириной N с помощью цикла for
"""

n = int(input("Enter the width of the triangle:"))
for i in range(n):
    print(" " * (n-i-1) + "*" * (i+1))

print('Triangle is drawn')
