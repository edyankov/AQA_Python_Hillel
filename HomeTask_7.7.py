"""
Задание 7
Дан файл в котором записан текст, необходимо вывести топ 5 строк которые чаще всего повторяются, пример:
'в' - 20 раз
'привет' - 10 раз
'как' - 9 раз
'у' - 7
'world' - 4
"""

with open('top_5_words.txt', 'r') as file:
    data = file.read()

result = {}
for word in data.split():
    word = word.lower()
    if word not in result:
        result[word] = 1
    else:
        result[word] += 1
t = [(v, k,) for k, v in result.items()]
t.sort()
t = t[-5:]
t.reverse()
for number, word in t:
    print(f"{word} - {number} times")

print("End")
