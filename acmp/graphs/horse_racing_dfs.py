n, k = map(int, input().split())
# победит ли лошадь под номером k?
k -= 1

matrix = [[0]*n for i in range(n)]


while True:
    data = input().split()
    if len(data) == 1:
        break
    u, v = list(map(int, data))
    u -= 1
    v -= 1
    if v == k:
        answer = 'NO'
    matrix[u][v] = 1


# по dfs спускаемся вглубь и смотрим, всех ли посетили
visited = [False]*n


def dfs(matrix, visited, k):
    visited[k] = True
    answer = 1

    for to in range(n):
        if visited[to] == False and matrix[k][to] == 1:
            answer += dfs(matrix, visited, to)

    return answer


answer = dfs(matrix, visited, k)

if answer == n and answer != 'NO':
    print('Yes')
else:
    print('No')
