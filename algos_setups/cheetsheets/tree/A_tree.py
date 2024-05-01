# Если у дерева нет ограничения на количество дочерних узлов (арности),
# то для хранения детей удобно завести массив:
class Node:
    def __init__(self, obj, children=None):
        self.obj = obj
        if children is not None:
            self.children = children
        else:
            self.children = []


# Бинарное дерево (не более двух потомков). Их обычно задают через два отдельных поля:
class Node:
    def __init__(self, obj, left=None, right=None):
        self.obj = obj
        self.left = left
        self.right = right

    # ЕСЛИ ДЕРЕВО ЯВЛЯЕТСЯ ДЕРЕВОМ ПОИСКА, ТО ПОИСК МОЖЕТ РАБОТАТЬ ВОТ ТАК:
    def find_node(self, root, obj):
        # Если мы пришли в поддерево, а его не существует,
        # значит, нужного элемента в дереве поиска нет
        if root is None:
            return None
        if self.obj < root.obj:
            return self.find_node(root.left, obj)
        if self.obj == root.obj:
            return root
        if self.obj > root.obj:
            return self.find_node(root.right, obj)

    # вставка (дерево поиска)
    def insert(root, key):
        if key < root.value:
            if root.left is None:
                root.left = Node(None, None, key)
            else:
                insert(root.left, key)
        if key >= root.value:
            if root.right is None:
                root.right = Node(None, None, key)
            else:
                insert(root.right, key)
        return

    # УДАЛЕНИЕ УЗЛА ИЗ ДЕРЕВА ПОИСКА
    """
ВРЕМЕННАЯ & ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ:
    Временная сложность алгоритма равна O(h), где h - высота дерева
    Пространственная сложность также равна O(h), которая используется для хранения стека вызовов

ПРИНЦИП РАБОТЫ:
    Имеется несколько случаев, которые алгоритм должен уметь обрабатывать (при наличии key в дереве):
    1) У узла нет дочерних элементов - самый простой случай, если в дереве только 1 узел - возвращаем None,
        если нет - удаляем узел, который необходимо обработать и возвращаем корень дерева
    2) У узла два потомка - находим минимальный элемент в правом поддереве, сохраняем его значение,
        потом рекурсивно удаляем этот элемент. Записанное ранее значение сохраняем в текущий узел.
    3) Удаляемый узел имеет одного потомка - ищем дочерний узел, если он не корень дерева - делаем его родительским. В противном
        случае установим дочерний узел как корень
"""

    def find(node, key):
        find_result = node  # тек. узел
        parent = None  # его родитель

        while find_result is not None and find_result.value != key:
            parent = find_result
            # если ключ меньше - ищем в левом поддереве
            # иначе ищем в правом
            if key < find_result.value:
                find_result = find_result.left
            else:
                find_result = find_result.right

        return find_result, parent

    def find_min(node):
        if node.left:
            return find_min(node.left)
        return node

    def remove(root, key):
        if root is None:
            return root

        find_result, parent = find(root, key)
        if find_result is None:
            return root

        # всего есть 3 случая:
        # 1: узел не имеет потомков
        # 2: узел имеет левого или правого потомка
        # 3: узел имеет обоих потомков

        if find_result.left is None and find_result.right is None:
            if find_result != root:
                if parent.left == find_result:
                    parent.left = None
                else:
                    parent.right = None
            else:
                root = None
        elif find_result.left is not None and find_result.right is not None:  # левый И правый потомок существует
            min_node = find_min(find_result.right)
            min_value = min_node.value

            remove(root, min_value)
            find_result.value = min_value
        else:  # существует 1 потомок (левый или правый)
            child = find_result.left
            if find_result.right is not None:
                child = find_result.right

            if find_result != root:
                if find_result == parent.left:
                    parent.left = child
                else:
                    parent.right = child
            else:
                root = child

        return root

    """
    Обход дерева
    Выделяют два вида обходов: прямой и обратной
    
    Прямой - порядок, которому интуитивно следует большинство людей. Сначала смотрим корень дерева,
    потом переводим взгляд на поддерево. В поддеревьях повторяем тот же алгоритм: сначала изучаем корень, потом - поддеревья
    *Порядок обхода детей не регламентируется, но обычно рассматривают слева-направо
    """
    # для дерева без заданной арности
    def print_forward(vertex):
        print(vertex.value)
        for child in vertex.children:
            print_forward(child)

        """
        Второй способ обхода - обратный.
        Он похож на прямой, за той лишь разницей, что сначала рассматриваются все поддеревья в любом порядке и только потом - корень поддерева.
        
        """
    def print_reversed(vertex):
        for child in vertex.children:
            print_reversed(child)
        print(vertex.value)

        """
        Есть еще один обход специально для бинарных деревьев - центрированный.
        Суть: сначала выводим все элементы одного поддерева. Потом корень. Потом элементы другого поддерева.
        У метода есть два варианта: LMR(left-middle-right) - сначала левое, потом центр, потом правое
        RML(right-middle-left) - сначала правое, потом центр, потом левое
        """
    def print_LMR(vertex):
        if not vertex.left is None:
            print_LMR(vertex.left)
        print(vertex.value)
        if not vertex.right is None:
            return print_LMR(vertex.right)
        # При LMR-обходе данные будут отсортированы от меньшего к большему
        # при RML-от большего к меньшему
