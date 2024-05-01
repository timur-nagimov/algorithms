"""
    Множество - структура, где элемент либо есть, либо нет.
    Множество имеет 3 операции:
        1. Добавлять элемент в множество
        2. Проверять его наличие
        3. Удалять элемент
        
    Реализация множества:
    Пусть есть какой-то набор элементов целых чисел.
    Можно сопоставлять введенному числу значение индекса из списка, но при этом число мы преобразуем в число от 0 до ...
"""

# Реализация (мульти)множества через двумер. список


class Multiset:
    def __init__(self, setsize):
        self.setsize = setsize
        self.myset = [[] for _ in range(setsize)]

    def add(self, x):
        self.myset[x % self.setsize].append(x)

    def find(self, x):
        for now in self.myset(x % self.setsize):
            if now == x:
                return True
        return False

    def delete(self, x):
        xlist = self.myset[x % self.setsize]
        for i in range(len(xlist)):
            if xlist[i] == x:
                xlist[i], xlist[len(xlist) -
                                1] = xlist[len(xlist) - 1], xlist[i]
                xlist.pop()
                return
