import json
import os
import platform


"""4. Створити файл answers.py в якому створити Dict такого вигляду:
{'one': '1', 'two': '2', 'three': '3'}
та максимально коротким записом в коді поміняти місцями ключі та значення."""

source_dict = {"one": "1", "two": "2", "three": "3"}
reversed_dict = {value: key for key, value in source_dict.items()}

"""5. У файлі answers.py створити функцію, яка запише результат виконання коду з п.4 у новий файл answers.txt"""


def write_dict_in_file(data_dict: source_dict):
    with open('answers_dict.txt', 'w') as f:
        json.dump(data_dict, f)
    return f


write_dict_in_file(reversed_dict)

"""6. Створити файл test.txt; у файлі answers.py створити функцію, яка перейменує файл test.txt в залежності від того, 
яка у вас операційна система:
windows.txt -- MS Windows
linux.txt -- Linux
mac.txt -- MacOS"""


def rename_file_os():
    with open('test.txt', 'w') as f:
        f.write("this file will be renamed according to the operating system installed "
                "on the device where the code is run")

    system = platform.system()
    os_map = {'Windows': 'windows.txt', 'Linux': 'linux.txt', 'Darwin': 'mac.txt'}

    if system in os_map:
        os.rename('test.txt', os_map[system])
    else:
        print('Unknown OS')


rename_file_os()

"""7. Створити генератор, який буде інкрементувати число з кроком 1, починаючи з числа, 
яке передається як перший аргумент. Зупиняти своє виконання у випадку, якщо буде досягнуто значення, 
передане другим аргументом, незалежно від знаку (наприклад 10 або -10)"""


def increment(start: int, stop: int):
    if start < stop:
        while start <= stop:
            yield start
            start += 1
    else:
        while start >= stop:
            yield start
            start -= 1


for num in increment(-5, 10):
    print(num)

# num = increment(-5, 10)
# print(next(num))
# print(next(num))
# ....

"""8. Створти 3 класи: A, B, C. Клас B віднаслідувати від A; C - від B.
В кожному з класів має бути поле name з унікальним для цього класу значенням. Наприклад 'A', 'B' або 'C'.
* При зверненні до полів класу (не cтворюючи екземпляр), має друкуватись відповідний name
* При створенні екземпляру класу C, має бути надруковано в консоль значення поля name з класу A. 
Використовувати super."""


class A:
    name = 'A'

    def __init__(self):
        self.name = A.name


class B(A):
    name = 'B'

    def __init__(self):
        super().__init__()


class C(B):
    name = 'C'

    def __init__(self):
        super().__init__()


print(A.name)
print(B.name)
print(C.name)
c = C()
print(c.name)

"""9. Аргументи функцій: 
- показати (в answers.py) приклади використання args та kwargs"""


def multiply(*args):
    result = 1
    for arg in args:
        result *= arg
    return result


print(multiply(2, 3, 4, 5))  # виведе 120


def print_values(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")


print_values(name="John", age=30, city="New York")  # виведе name = John, age = 30, city = New York


def my_function(*args, **kwargs):
    print("Позиційні аргументи:")
    for arg in args:
        print(arg)
    print("\nІменовані аргументи:")
    for key, value in kwargs.items():
        print(f"{key} = {value}")


my_function(1, 2, 3, name="John", age=30, city="New York")


"""10. в answers.py написати функцію, яка буде відкривати json файл та змінювати в ньому обране поле (значення)."""


def update_json_file(file: str, field_to_update: str, new_value):
    with open(file) as f:
        data = json.load(f)

    data[field_to_update] = new_value

    with open(file, 'w') as f:
        json.dump(data, f, indent=4)


update_json_file('json_file.json', 'email', "johndoe@gmail.com")
