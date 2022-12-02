"""
Задание 7:
Пользователь вводит текст нужно вывести количество чисел в этом тексте
Пример:
> 'Lorem 222 ipsum, 123 dolor 1 sit amet
Количество чисел: 3
"""

import re

string = input("Enter your text: ")
cnt = len(re.findall(r"\d+", string))
if cnt:
    print("Amount of numbers in text: ", cnt)
else:
    print("No numbers found in text")

print("End")
