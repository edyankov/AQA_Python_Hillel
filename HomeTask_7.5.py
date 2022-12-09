"""
Задание 5
Дан файл с произвольным текстом, нужно найти количество слов в файле и вывести пользователю
"""

file = open('count_of_words.txt', 'r')
data = file.read()

print(len(data.split()))
file.close()

print("End")
