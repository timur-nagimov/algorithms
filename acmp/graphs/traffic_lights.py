# n - перекрестки, m - тоннели
n, m = map(int, input().split())

cor_list = [[] for _ in range(n)]

for i in range(m):
    i, j = map(int, input().split())
    cor_list[i-1].append(j-1)
    cor_list[j-1].append(i-1)


for i in range(len(cor_list)):
    print(len(cor_list[i]), end=' ')
