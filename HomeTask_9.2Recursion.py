"""
Написать функцию, которая принимает целое число - number.
Функция должна возвращать 'yes' если number является степенью двойки, иначе 'no'.
Запрещено пользоваться функцией или оператором возведение в степень.
Пример:
is_power_of_two(256) # 'yes' потому что 2 в 8 степени это 256
is_power_of_two(125) # 'no' потому что это не степень двойки
"""


def is_power_of_two(number):
    current = number / 2
    number = int(current)
    if current != number or number == 0:
        return 'No'
    if number == 1:
        return 'Yes'
    return is_power_of_two(number)


print(is_power_of_two(256))
