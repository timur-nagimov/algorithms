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
