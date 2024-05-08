from collections import deque
from queue import Queue

n, m = map(int, input().split())
adj_list = [[] for _ in range(n)]
color = ['white']*n
previous = [None]*n


def BFS(s):
    planned = Queue()
    planned.put(s)
    color[s] = 'gray'

    # distance[s] = 0
    while not planned.empty():
        u = planned.get()
        print(u + 1, end=' ')
        for v in adj_list[u]:
            if color[v] == 'white':
                # distance[v] = distance[u] + 1
                previous[v] = u
                color[v] = 'gray'
                planned.put(v)
        color[u] = 'black'


for _ in range(m):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    adj_list[i].append(j)
    adj_list[j].append(i)

start_vertex = int(input()) - 1

BFS(start_vertex)
