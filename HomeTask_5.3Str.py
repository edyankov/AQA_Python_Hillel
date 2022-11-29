"""
Задание 3:
Пользователь вводит строку. Если она начинается на 'abc', то заменить их на 'www', иначе добавить в конец строки 'zzz'.
"""

string = str(input("Enter your string:"))
if string.startswith('abc'):
    print(string.replace('abc', 'www'))
else:
    print(f'{string}zzz')

print("End")
