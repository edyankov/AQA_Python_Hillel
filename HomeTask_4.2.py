"""
Вывести треугольник #2 с шириной N с помощью цикла for
"""

n = int(input("Enter the width of the triangle:"))
for i in range(n):
    print("*" * (i+1))

print('Triangle is drawn')
