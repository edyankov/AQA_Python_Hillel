"""
Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь,
в котором каждый элемент списка является и ключом и значением.
Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.
"""


def to_dict(lst):
    try:
        [hash(i) for i in lst]
    except Exception as e:
        return "Error: mutable element detected"
    return {element: element for element in lst}


print(to_dict(['Hillel', 'Apple', (56, -9), 9.26]))

print(to_dict(['Hillel', 'Apple', (56, -9), 9.26, {'a': 's'}]))
