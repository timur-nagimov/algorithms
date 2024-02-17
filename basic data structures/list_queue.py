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
