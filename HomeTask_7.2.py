"""
Задание 2
Запросить у пользователя текст и записать его в файл data.txt
"""

file = open('data.txt', 'w+')
try:
    text = input("Enter text to write to file: ")
    file.write(text)
    print("Entered text: ", text)
finally:
    file.close()

print("End")
