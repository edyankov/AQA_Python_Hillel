"""
Задание 1:
Пользователь вводит слово, если это слово является палиндромом, то вывести '+', иначе '-'
"""

slovo = str(input("Enter palindromic slovo:"))
if slovo == slovo[::-1]:
    print("+")
else:
    print("-")

print("End")
