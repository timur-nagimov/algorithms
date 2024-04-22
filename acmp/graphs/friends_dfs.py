# s - номер вершины для которой считаем кол-во друзей
# друзья друзей тоже друзья

n, s = map(int, input().split())
s -= 1

matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))


def dfs(matrix, visited, s, n):
    visited[s] = True
    global answer
    answer += 1

    for to in range(n):
        if matrix[s][to] == 1 and visited[to] == False:
            dfs(matrix, visited, to, n)


answer = 0
visited = [False]*n
dfs(matrix, visited, s, n)

print(answer-1)
