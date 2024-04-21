n = int(input())

cor_matrix = []

for i in range(n):
    cor_matrix.append(list(map(int, input().split())))


ans = 0
for i in range(n):
    for j in range(i+1, n):
        if cor_matrix[i][j] == 1:
            ans += 1

print(ans)
