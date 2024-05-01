class Deque:
    def __init__(self, max_size):
        self.data = [None] * max_size
        self.max_size = max_size
        self.size = 0
        self.head = max_size - 1
        self.tail = 0

    def is_empty(self):
        return self.size == 0

    def push_back(self, x):
        if self.size < self.max_size:
            self.data[self.tail] = x
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
        else:
            self.error_message()

    def push_front(self, x):
        if self.size < self.max_size:
            self.data[self.head] = x
            self.head = (self.head - 1 + self.max_size) % self.max_size
            self.size += 1
        else:
            self.error_message()

    def pop_front(self):
        if self.is_empty():
            self.error_message()
        else:
            self.head = (self.head + 1) % self.max_size
            x = self.data[self.head]
            self.size -= 1
            print(x)

    def pop_back(self):
        if self.is_empty():
            self.error_message()
        else:
            self.tail = (self.tail - 1 + self.max_size) % self.max_size
            x = self.data[self.tail]
            self.size -= 1
            print(x)

    def error_message(self):
        raise Exception("Deque is full or empty")


# дек на двусвязном списке
class Item:
    '''Item - узел двусвязного списка (класс)'''

    def __init__(self, next__item=None, prev__item=None, elem=None):
        self.next__item = next__item
        self.prev__item = prev__item
        self.elem = elem


class DoubleLinkedList:
    '''DoubleLinkedList - двусвязный список (класс)'''

    def __init__(self, head=None, tail=None, length=0):
        self.head = head
        self.tail = tail
        self.length = length

    def push(self, elem):
        '''добавляет элемент в конец списка'''
        if self.tail is None:  # length == 0
            item = Item(None, None, elem)
            self.head = item
            self.tail = self.head
            self.length = 1
        else:
            item = Item(None, self.tail, elem)
            self.tail.next__item = item
            self.tail = item
            self.length += 1

    def pop(self):
        '''убирает элемент из конца списка'''
        try:
            if self.tail is None:  # length == 0
                raise Exception("There is nothing to pop!")  # empty list
            else:
                self.tail = self.tail.prev__item
                if self.tail is not None:
                    self.tail.next__item = None
                self.length -= 1
        except Exception as error:
            print("Caught this error: " + error.args[0])

    def unshift(self, elem):
        '''добавляет элемент в начало списка'''
        if self.head is None:
            item = Item(None, None, elem)
            self.head = item
            self.tail = self.head
            self.length = 1
        else:
            item = Item(self.head, None, elem)
            self.head.prev__item = item
            self.head = self.head.prev__item
            self.length += 1

    def shift(self):
        '''убирает элемент из начала списка'''
        try:
            if self.head is None:  # length == 0
                raise Exception("There is nothing to shift!")  # empty list
            else:
                self.head = self.head.next__item
                if self.head is not None:
                    self.head.prev__item = None
                self.length -= 1
        except Exception as error:
            print("Caught this error: " + error.args[0])

    def len(self):
        '''возвращает длину списка'''
        return self.length

    def delete(self, elem):
        '''удаляет элемент из списка (первое вхождение с начала)'''
        if self.head is None:  # length == 0
            pass  # return
        elif self.head.elem == elem:
            self.shift()
        else:
            cur = self.head.next__item
            while cur is not None:
                if (cur.elem == elem) and (cur.next__item is not None):
                    temporary_item = cur.prev__item.next__item
                    cur.prev__item.next__item = cur.next__item.prev__item
                    cur.next__item.prev__item = temporary_item
                    self.length -= 1
                    break  # return
                elif (cur.elem == elem) and (cur.next__item is None):
                    cur.prev__item.next__item = None
                    self.tail = cur.prev__item
                    self.length -= 1
                    break  # return
                else:
                    cur = cur.next__item

    def contains(self, elem):
        '''проверяет, входит ли элемент в список'''
        if self.head is None:  # length == 0
            return False
        elif self.head.elem == elem:
            return True
        else:
            cur = self.head.next__item
            while cur is not None:
                if cur.elem == elem:
                    return True
                else:
                    cur = cur.next__item
            return False

    def first(self):
        '''возвращает первый Item в списке'''
        return self.head

    def last(self):
        '''возвращает последний Item в списке'''
        return self.tail

# some extra functions
    def first_elem(self):
        '''возвращает первый Item.elem в списке'''
        return self.head.elem

    def last_elem(self):
        '''возвращает последний Item.elem в списке'''
        return self.tail.elem
