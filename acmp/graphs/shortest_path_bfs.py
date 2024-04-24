from collections import deque


n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
start, finish = map(int, input().split())

edges = [[] for i in range(n)]
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            edges[i].append(j)


dist = [None]*n
start_vertex = start - 1
dist[start_vertex] = 0
queue = deque([start_vertex])

while queue:
    cur_v = queue.popleft()
    for i in edges[cur_v]:
        if dist[i] is None:
            dist[i] = dist[cur_v] + 1
            queue.append(i)


if dist[finish-1] is not None:
    print(dist[finish-1])
else:
    print(-1)
