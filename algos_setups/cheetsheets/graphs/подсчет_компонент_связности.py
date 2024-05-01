# DFS, но красим вершины в одном компоненте в одинак. цвета
import sys
sys.setrecursionlimit(15000000)

n, m = map(int, input().split())
adjacency_list = [[] for x in range(n)]
component_count = 0

color = [-1] * n
list_by_colors = []

for _ in range(m):
    top, edge = map(int, input().split())
    adjacency_list[top-1].append(edge-1)
    adjacency_list[edge-1].append(top-1)
for i in range(n):
    adjacency_list[i].sort(reverse=False)


def DFS(v):
    global component_count, list_by_colors
    color[v] = 'grey'
    for w in adjacency_list[v]:
        if color[w] == -1:
            DFS(w)
    list_by_colors[component_count].append(v+1)
    color[v] = component_count


for i in range(0, n):
    if color[i] == -1:
        list_by_colors.append([])
        DFS(i)
        list_by_colors[component_count].sort()
        component_count += 1

print(component_count)
for one_color in list_by_colors:
    for w in one_color:
        print(w, end=' ')
    print()
