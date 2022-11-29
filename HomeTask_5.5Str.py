"""
Задание 5:
Написать валидатор для почты.
Пользователь вводит почту, а программа должна проверить, что в почте есть символ '@' и '.',
и если это так, то вывести "YES", иначе "NO"
"""

email = str(input("Enter your email address:"))
has_at_sign = email.find('@') != -1
has_dot = email.find('.') != -1
if has_at_sign and has_dot:
    print("YES")
else:
    print("NO")

print("End")
