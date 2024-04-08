class Stack:
    """
    Структура данных, работает по принципу LIFO.
    Стек удобно хранить как массив, но если элементов
    много, лучше использовать связный список.
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]
