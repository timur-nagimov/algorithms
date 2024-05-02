import os
import sys

sys.setrecursionlimit(10**5)

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root, min_val=float('-inf'), max_val=float('inf')) -> bool:
    if root is None:
        return True

    if not (root.value > min_val and root.value < max_val):
        return False

    return solution(root.left, min_val, root.value) and solution(root.right, root.value, max_val)


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)


if __name__ == '__main__':
    test()
