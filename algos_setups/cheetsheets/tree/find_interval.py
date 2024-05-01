"""
    Бин. дерево поиска можно использовать для поиска элементов в интервале.
    Допустим, мы хотим вывести все товары с ценой от 1500 до 1900р.

    Первым делом ищем среди товаров стоимостью больше 1500р самый дешевый. Для этого применим стандартный алгоритм поиска с небольшой модификацией:
    * Если корень дерева меньше искомого элемента 1500, поиск производится в правом поддереве
    * Если корень дерева больше или равен искомому элементу 1500, мы рекурсивно повторяем процедуру поиска в левом поддереве
    * Если в левой половине элементов не нашлось, значит, корень дерева является первым элементом, который имеет стоимость больше либо равную 1500.
    """
# Втупую можно пройти все дерево, добавить подходящие и отсортировать


# Тут по умному
import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value


def print_range(node, l, r):
    if node is None:
        return

    if node.value < l:
        print_range(node.right, l, r)
    elif node.value > r:
        print_range(node.left, l, r)
    else:
        print_range(node.left, l, r)
        print(node.value)
        print_range(node.right, l, r)


def test():
    node1 = Node(None, None, 2)
    node2 = Node(None, node1, 1)
    node3 = Node(None, None, 8)
    node4 = Node(None, node3, 8)
    node5 = Node(node4, None, 9)
    node6 = Node(node5, None, 10)
    node7 = Node(node2, node6, 5)
    print_range(node7, 2, 8)
    # expected output: 2 5 8 8


if __name__ == '__main__':
    test()
