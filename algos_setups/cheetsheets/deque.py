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
