"""
Задание 1
Дан файл с произвольным текстом, необходимо найти все числа в файле и записать в список numbers
"""

import re

r = r'\d+'

file = open('file.txt', 'r')
numbers = file.read()

print('List of numbers: ', re.findall(r, numbers))

print('End')
