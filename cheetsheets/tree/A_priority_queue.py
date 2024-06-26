"""
Приоритетная очередь - это очередь, элементы которой имеют приоритет.
Бинарная куча - двоичное дерево, которое соответствует следующим условиям:
    * Ключ в любой вершине не меньше(если куча для максимума), чем значения её потомков.
      Это свойство гарантирует, что в вершине находится самый приоритетный элемент
    * На i-м слое 2^i вершин, кроме последнего. Для последнего слоя это условие может не соблюдаться.
      Слои нумеруются с нуля. Это свойство соответствует почти полноте. Т.к, чтобы на i+1 слое было 2^(i+1) вершин,
      у каждой из вершин i-го слоя должно быть ровно 2 ребёнка.
    * Все слои, кроме последнего, уже заполнено полностью, в них вообще нет дыр.
      Последний слой заполняется элементами слева направо.
      Поэтому все элементв лежат в массиве от начала и до конца
      
    Другое название Бинарной кучи - пирамида
    
    Вставка и удаление в приоритетную очередь.
    Для поддержания свойств бинарной кучи, необходимо правильно обрабатывать модифицирующие действия:
    * Вставку элемента в кучу
    * Извлечение с удалением элемента из кучи
    
    ВСТАВКА ЭЛЕМЕНТА:
    Во время вставки элемента в конец кучи, может нарушиться свойство, по которому значения дочерних узлов должны быть больше родительских (или меньше).
    Для исправления необходимо менять местами узлы до тех пор, пока дочерний больше, чем родительский.
    Операция восстановления свойств кучи при вставке нового элемента называется "просеивание вверх", или sift_up.
    Т.к при вставке на каждом уровне проводим только одно сравнение элемента, а куча имеет высоту logN, то вставка происходит за O(logN).
    
    УДАЛЕНИЕ ЭЛЕМЕНТА:
    Заберем самый приоритетный элемент из пирамиды. Для того, чтобы в ней не появились дыры, на место извлеченного элемента поставим последний элемент из кучи.
    Для восстановления свойств кучи при удалении используется "просеивание вниз".
    Рассмотрим текущий узел и его дочерние элементы. Если текущий узел - самый приоритетный из них, ничего не меняем.
    Иначе меняем текущий элемент с максимально приоритетным - он должен оказаться выше. Делаем так до конца.
    Таким образом, есть два критерия завершения процедуры восстановления:
    1. Если значение текущего узла больше, чем значения его потомков
    2. Если у текущего узла отсутствуют потомки.
    Удаление тоже работает за O(logN)
    
"""


# Для максимума
class BinaryHeap:
    def __init__(self):
        self.heap = [-1]

    # Дополнительное пояснение по просеиванию вверх:
    # Вставка элемента происходит в конец кучи. Т.е создается новая ячейка и он записывается туда
    # Очевидно, что после такой вставки свойство бинарной кучи по наличию макс/мин. элемента в голове не гарантируется.

    # Как же исправить эту ситуацию? В целом, достаточно просто:
    # Если дочерний узел больше(или меньше в минимальной куче) родительского - меняем их местами.
    # Повторяем действие до тех пор, пока элемент не будет меньшим(большим), или пока он не встанет в голову.
    def sift_up(self, index):
        # Если дошли до головы - останавливаемся
        if index == 1:
            return

        # Смотрим родительский узел(по условию он хранится по индексу_дочернего//2)
        parent_index = index // 2
        # Если элемент действительно больше - меняем их местами
        if self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            # Запускаем просеивание вверх для этого же элемента, но уже на новом месте
            self.sift_up(parent_index)

    def heap_add(self, key):
        self.heap.append(key)
        index = len(self.heap) - 1
        self.sift_up(index)

    # Дополнительное пояснение по просеиванию вниз:
    # Самый приоритетный элемент из кучи забирается из головы. На его место мы ставим ПОСЛЕДНИЙ элемент кучи.
    # Опять же очевидно, что свойство кучи будет нарушено.
    # Просеивание вниз восстанавливает свойство:
    # Рассмотрим текущий узел и его дочерние элементы. Если он узел имеет самый большой (или маленький в мин.куче) приоритет - ничего не меняем.
    # В противном случае меняем текущий элемент с максимально приоритетным (или минмально в мин.куче) - он должен оказаться выше.
    # Повторяем до тех пор, пока:
    # 1) Значение текущего узла меньше(больше в мин.куче), чем значения его потомков
    # 2) Пока у текущего узла есть потомки
    def sift_down(self, index):
        heap_max_index = len(self.heap) - 1
        # индекс левого дочернего элемента
        left = index*2
        # правого
        right = index*2 + 1

        # если нет дочерних узлов - выходим
        if left > heap_max_index:
            return

        # right < heap_max_index проверяет, что есть оба дочерних узла
        # второе условие ищет макс. элемент среди них
        if right <= heap_max_index and self.heap[right] > self.heap[left]:
            index_largest = right
        else:
            index_largest = left

        # отправляем максимум на вершину кучи и рекурсивно завпускаем просеивание в ребенке
        if self.heap[index_largest] > self.heap[index]:
            self.heap[index_largest], self.heap[index] = self.heap[index], self.heap[index_largest]
            self.sift_down(index_largest)

    def pop_max(self):
        if len(self.heap) == 1:
            return None
        result = self.heap[1]
        self.heap[1] = self.heap[len(self.heap) - 1]
        self.heap.pop()  # удаляем ласт. элемент который вставили в голову
        self.sift_down(1)
        return result


"""
    EXTRA:
    Просеивания без использования рекурсий
    В коде ниже дополнительно достается индекс позиции, куда встал элемент
"""


def sift_down(heap, idx):
    size = len(heap) - 1
    left, right = -1, -1

    return_index = idx
    while True:
        index_largest = idx
        left = 2 * idx
        right = 2 * idx + 1
        if size < left:
            break

        if right <= size and heap[left] < heap[right]:
            index_largest = right
        else:
            index_largest = left

        if heap[idx] < heap[index_largest]:
            heap[idx], heap[index_largest] = heap[index_largest], heap[idx]
            return_index = index_largest
        idx = index_largest
    return return_index


def sift_up(heap: object, idx: object) -> object:
    return_index = idx
    while (idx != 1):
        parent_index = idx//2
        if heap[idx] > heap[parent_index]:
            return_index = parent_index
            heap[idx], heap[parent_index] = heap[parent_index], heap[idx]
        idx = parent_index
    return return_index
