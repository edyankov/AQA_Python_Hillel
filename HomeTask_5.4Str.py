"""
Задание 4:
Пользователь вводит текст, удалить в тексте все цифры и вывести строку пользователю.
"""

string = str(input("Enter your string with numbers:"))
alphabetic_string = ''.join([i for i in string if not i.isdigit()])
print(alphabetic_string)

print("End")
