"""
    Очередь(queue) - с труктура данных, работающая по принципу FIFO (First In - First Out)
    В самой простой реализации очереди достаточно двух методов:
        1. push(x) - добавляет элемент x в конец очереди
        2. pop() - удаляет элемент из начала очереди
    
    Варианты реализации очереди:
        1. Очередь на массиве
            - Из начала удалять сложно
            - Удаление каждого элемента требует O(n) операций
            
        2. Очередь на массиве оптимизированная
            Вместо того, чтобы сдвигать все элементы массива после удаления, мы будем сдвигать 'начало'
            Т.е head после удаления будет указывать на второй элемент
            - Требуется много памяти, т.к указатель может улететь очень-очень далеко.
            
        
        3. Очередь на двух стеках
            Заведем push_stack и pop_stack.
            При добавлении элементов - добавляем в push_stack
            Когда надо удалить - достаем из pop_stack.
            Если pop_stack пуст - добавляем туда все элементы из push_stack
            
        4. Очередь на кольцевом буфере
            Сворачиваем очередь
            - Приходится задавать ограничение на макс. размер очереди (K)
            
            Когда удаляем элемент - head + 1
            Когда добавляем - tail - 1
            
            Когда head или tail достигнут K - сдвигаем их. 
            Т.е в каждый момент времени когда меняются координаты, берем их координаты по % K (модулю K)
        
        5. Очередь на связном списке
            Пожалуй, самая адекватная реализация

"""

# 1-2: Очереди на массивах - тривиально, без реализации


# 3. Очередь на двух стеках
from stack import Stack


class Queue:
    def __init__(self):
        self.push_stack = Stack()
        self.pop_stack = Stack()
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        self.push_stack.push(x)
        self.size += 1

    def pop(self):
        if self.is_empty():
            return ValueError("Очередь пуста")
        if self.pop_stack.size() == 0:
            while self.push_stack.size():
                self.pop_stack.push(self.push_stack.pop())
        x = self.pop_stack.pop()
        self.size -= 1
        return x


# 4. Очередь на кольцевом буфере
class RingQueue:
    def __init__(self, max_n):
        self.queue = []
        self.head = None
        self.tail = None
        self.max_n = max_n
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail+1) % self.max_n
            self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.head = (self.head+1) % self.max_n
        self.size -= 1
        return x  # noqa: R504


# 5. Очередь на связном списке
class Node:
    def __init__(self, value: int, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.value = value


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self):
        if self.size == 0:
            return None

        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value  # noqa: R504

    def put(self, x):
        node = Node(x)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        self.size += 1

    def get_size(self):
        return self.size


def main():
    my_queue = Queue()
    n = int(input())

    for _ in range(n):
        command = input().split()
        if command[0] == 'put':
            my_queue.put(command[1])
        elif command[0] == 'get':
            returned_elem = my_queue.get()
            if returned_elem is None:
                print('error')
                continue
            print(returned_elem)
        elif command[0] == 'size':
            print(my_queue.get_size())
        else:
            raise AttributeError()


if __name__ == '__main__':
    main()
