"""
Задание 3
Запросить у пользователя число N и запросить N чисел у пользователя, потом записать их в файл numbers.txt через пробел
"""

file = open('numbers.txt', 'w')

numbers_count = input("Enter size of numbers: ")

numbers = []
for i in range(int(numbers_count)):
    numbers.append(input(f"Enter {i} number: "))

print(numbers)

file.write(' '.join(numbers))
file.close()

print("End")
