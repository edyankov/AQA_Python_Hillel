"""
Задание 7:
Пользователь вводит текст нужно вывести количество чисел в этом тексте
Пример:
> 'Lorem 222 ipsum, 123 dolor 1 sit amet
Количество чисел: 3
"""

import re

text = input("Enter your text: ")
count = len(re.findall(r"\d+", text))
if count:
    print("Amount of numbers in text: ", count)
else:
    print("No numbers found in text")

print("End")
