"""
Задание 4
Сгенерировать 100 рандомных чисел и записать их в файл random_numbers.txt, где одна строка = одно число
"""

import random

with open('random_numbers.txt', 'w') as file:
    numbers = random.sample(range(1, 10000), 100)
    lines = [f"{number}\n" for number in numbers]
    file.writelines(lines)

print("End")
