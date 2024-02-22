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
