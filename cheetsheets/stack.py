"""
    Очередь(queue) - с труктура данных, работающая по принципу FIFO (First In - First Out)
    В самой простой реализации очереди достаточно двух методов:
        1. push(x) - добавляет элемент x в конец очереди
        2. pop() - удаляет элемент из начала очереди
"""


# Стек с реализацией поиска максимального элемента за O(1)
class StackMax:
    def __init__(self):
        self.arr = []
        self.max_arr = []
        self.maximum = None

    def push(self, value):
        self.arr.append(value)
        if self.maximum is None or self.maximum < value:
            self.maximum = value
        self.max_arr.append(self.maximum)

    def pop(self):
        if self.get_length() == 0:
            print('error')
        else:
            self.arr.pop()

            self.max_arr.pop()
            self.maximum = None if self.get_length() == 0 else self.max_arr[-1]

    def get_max(self):
        print(self.maximum)

    def top(self):
        if self.get_length() == 0:
            print('error')
        else:
            print(self.arr[-1])

    def get_length(self):
        return len(self.arr)
