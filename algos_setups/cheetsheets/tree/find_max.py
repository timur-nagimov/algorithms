import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root, max_val=float('-inf')) -> int:
    max_val = max(max_val, root.value)

    if root.left is not None:
        max_val = solution(root.left, max_val)
    if root.right is not None:
        max_val = solution(root.right, max_val)

    return max_val


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3


if __name__ == '__main__':
    test()
