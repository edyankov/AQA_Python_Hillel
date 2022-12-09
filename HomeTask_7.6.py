"""
Задание 6
Дан файл в котором записаны числа через пробел, необходимо вывести пользователю сумму этих чисел
"""

with open('sum_of_numbers.txt', 'r') as f:
    data = f.read()
    result = sum(map(int, data.split()))
    print(result)

print("End")
