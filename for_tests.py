class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val):
        if self.head is None:
            self.head = self.tail = Node(val)
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

    def pop(self):
        if self.head is None:
            raise RuntimeError('Queue is empty')
        head_val = self.head.val
        self.head = self.head.next
        return head_val


queue = Queue()
queue.push(1)
queue.push(3)
print(queue.pop())
queue.push(15)
print(queue.pop())
queue.push(1)
queue.push(11)
queue.push(-13)
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())
