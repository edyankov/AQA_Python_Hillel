"""
Необходимо создать класс Human с атрибутами:
- name
- surname
- age
- phone
- address
Атрибуты должны заполняться в методе __init__
Так-же нужно написать методы:
get_info(self) - который возвращает словарь в котором находится информация о человеке
call(self, phone_number) - который будет выводить "{self.phone} вызывает абонента {phone_number}"
Нужно создать 3 объекта класса Human и вызвать у них метод get_info
"""


class Human:
    def __init__(self, name, surname, age, phone, address):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.address = address

    def get_info(self):
        return self.__dict__
        # info_items = ['name', 'surname', 'age', 'phone', 'address']
        # return {i: getattr(self, i) for i in info_items}

    def call(self, phone_number):
        return f"{self.phone} calls the subscriber {phone_number}"


Human_I = Human('Boris', 'Lewis', '32', '496-251-8419', 'Denver')
Human_II = Human('Emilio', 'Gan', '45', '102-665-1932', 'New York')
Human_III = Human('Steven', 'Wang', '36', '230-459-3242', 'San Diego')

print(Human_I.get_info())
print(Human_I.call('425-426-8902'))
print(Human_II.get_info())
print(Human_II.call('434-624-8356'))
print(Human_III.get_info())
print(Human_III.call('861-431-7659'))
