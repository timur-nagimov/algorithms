"""
    У алгоритма DFS много применений. Например, он позволяет определить наличие цикла в графе и найти его.
    Можно работать с ориентированным графом: идти по графу и запоминать все посещённые вершины. Например, заносить их в список.
    Как только встретим какую-то вершину второй раз, сделаем вывод, что цикл в графе есть.
    
    Но есть другой способ. Можно воспользоваться массивом цветов вершин. Если при проверке смежных по исходящим дугам вершин очередная вершина
    окажется серой - цикл есть.
    
    * черная вершина не указывает на цикл.
    Если вершина черная - от нее нет пути до текущей вершины, ведь мы красим узел в черный после того, как все доступные из нее вершины были обработаны.
    В неориентированном графе так определить цикл не получится: нужно проверять все смежные вершины, кроме одной - той, из которой мы только пришли.
"""

# Можно завести два массива: Entry - момент входа и Leave - момент выхода.
# Ячейка вершины в массиве Entry обновляется, когда вершина красится в серый цвет,
# а в Leave - когда перекрашивается в черный


# ниже - подсчет времени входа и выхода в графах, не поиск цикла!
import sys
color = ['white', 'white', ...]
time = 0
entry = [None, None ...]
leave = [None, None ...]


sys.setrecursionlimit(15000000)

n, m = map(int, input().split())
adjacency_list = [[] for x in range(n)]

color = ['white'] * n
entry = [None] * n
leave = [None] * n

for _ in range(m):
    top, edge = map(int, input().split())
    adjacency_list[top-1].append(edge-1)
for i in range(n):
    adjacency_list[i].sort(reverse=False)

time = -1


def DFS(v):
    global time
    time += 1
    entry[v] = time
    color[v] = 'gray'
    for w in adjacency_list[v]:
        if color[w] == 'white':
            DFS(w)
    time += 1
    leave[v] = time
    color[v] = 'black'


DFS(0)
for i in range(len(entry)):
    print(entry[i], leave[i])
