"""
Задание 1:
Запросить у пользователя 5 чисел и записать их в список
"""

numbers_list = []
for i in range(5):
    numbers = int(input(f"Enter your numbers #{i}: "))
    numbers_list.append(numbers)

print(numbers_list)

print("End")
