class Node:
    """
    Связный список может удалять и вставлять элементы в начало
    без передвижения остальных.
    Минусы:
    Элементы хранятся в памяти последовательно,
    и поэтому получить элемент за O(n) нельзя.
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def print_linked_list(vertex):
    while vertex:
        print(vertex.value, end='->')
        vertex = vertex.next
    print('None')


# Операции со связными списками
def get_node_by_index(node, index):
    while index:
        node = node.next
        index -= 1
    return node


# Вставка элемента
def insert_node(head, index, value):
    new_node = Node(value)
    if index == 0:
        new_node.next = head
        return new_node

    prev_node = get_node_by_index(head, index-1)
    new_node.next = prev_node.next
    prev_node.next = new_node
    return head
