n, m = map(int, input().split())

cor_list = [[] for i in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    cor_list[u-1].append(v)

print(n)
for i in range(n):
    ans = []
    for j in sorted(cor_list[i]):
        ans.append(j)
    print(len(ans), ' '.join(map(str, ans)))
