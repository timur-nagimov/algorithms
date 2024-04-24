import heapq as hq

n, s, f = map(int, input().split())
s -= 1
f -= 1

edges = [[] for _ in range(n)]
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if i != j and line[j] != -1:
            edges[i].append((j, line[j]))


def dj(edges, n, s, f):
    INF = 10**9
    dist = [INF]*n
    dist[s] = 0
    FROM = [-1]*n

    heap = []
    hq.heappush(heap, (dist[s], s))
    while heap:
        vertex_info = hq.heappop(heap)
        v = vertex_info[1]

        # если через другие вершины уже нашли кратчайший путь
        if dist[v] < vertex_info[0]:
            continue

        # рассматриваем все связанные с v вершины
        for i in range(len(edges[v])):
            to = edges[v][i][0]
            w = edges[v][i][1]

            if dist[to] > dist[v] + w:
                dist[to] = dist[v] + w
                FROM[to] = v

                hq.heappush(heap, (dist[to], to))

    if dist[f] != INF:
        ans = []
        vertex = f
        while vertex != -1:
            ans.append(vertex)
            vertex = FROM[vertex]

        for i in range(len(ans)-1, -1, -1):
            print(ans[i]+1, end=' ')
    else:
        print(-1)


dj(edges, n, s, f)
