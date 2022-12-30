"""
Написать итератор ReverseIterator который принимает список любых объектов и итерируется по ним в обратном порядке.
Важно: Нужно использовать аннотации.
Пример:

it = ReverseIterator([1, 2, 3, 4, 5])

next(it)  # 5
next(it)  # 4
next(it)  # 3
"""


class ReverseIterator:
    def __init__(self, data: list[any]):
        self.data = data
        self.index = len(data)

    def __iter__(self) -> 'ReverseIterator':
        return self

    def __next__(self) -> any:
        self.index -= 1
        if self.index < 0:
            raise StopIteration
        return self.data[self.index]


itr = ReverseIterator([1, 2, 3, 4, 5])
print("next(itr) #", next(itr))
print("next(itr) #", next(itr))
print("next(itr) #", next(itr))
print("next(itr) #", next(itr))
print("next(itr) #", next(itr))
