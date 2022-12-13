"""
Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент.
В исходном списке минимум 2 элемента.
"""


def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst


print(change([1, 2]))
print(change([1, 2, 3, 4, 5]))
print(change(['n', 'y', 't', 'h', 'o', 'P']))
