n = int(input())

matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))


ans_arr = []
for i in range(n):
    ans = 0
    for j in range(n):
        if matrix[i][j] == 1:
            ans += 1
    ans_arr.append(ans)
    ans = 0


print(' '.join(map(str, ans_arr)))
