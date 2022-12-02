"""
Задание 7:
Пользователь вводит текст нужно вывести количество чисел в этом тексте
Пример:
> 'Lorem 222 ipsum, 123 dolor 1 sit amet
Количество чисел: 3
"""

text = input("Enter your text: ")
digit_counter = 0
for i in text:
    if i.isdigit():
        digit_counter += 1
if digit_counter == 0:
    print("No numbers found in text")
else:
    print("Amount of numbers in text: ", digit_counter)

print("End")
