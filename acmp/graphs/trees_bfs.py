from collections import deque

# дан неориентированный граф в виде матрицы смежности
# проверить, является ли он деревом

n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

is_tree = True
if n > 1:
    visited = [False] * n
    deq = deque([0])  
    visited[0] = True
    parent = [-1] * n  # Для отслеживания родительских вершин
    edge_count = 0  # Счетчик ребер
    is_tree = True

    while deq:
        cur_v = deq.popleft()
        for i in range(n):
            if matrix[cur_v][i] == 1:
                if not visited[i]:
                    visited[i] = True
                    deq.append(i)
                    parent[i] = cur_v
                    edge_count += 1
                elif parent[cur_v] != i:
                    is_tree = False  # Найден цикл

    is_tree = is_tree and edge_count == n - 1 and all(visited)

print('YES' if is_tree else 'NO')
