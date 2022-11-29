"""
Задание 2:
Пользователь вводит текст и слово которое нужно найти, если это слово есть в тексте, вывести 'YES', иначе 'NO'

Come and visit our Showroom at Frank Borda Ltd, Gala Centre and choose from the latest Skoda Models.
"""

text = str(input("Enter your text:"))
if text.find("Skoda") != -1:
    print("YES")
else:
    print("NO")

print("End")
