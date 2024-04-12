# https://codeforces.com/edu/course/2/lesson/6/2/practice/contest/283932/problem/B

n, k = map(int, input().split())
ropes = []
for _ in range(n):
    ropes.append(int(input()))


def ok(ropes, k, mid):
    summa = 0
    for rope in ropes:
        summa += rope // mid  # целые веревки
    return summa >= k


l = 0
r = 10**12
ans = 0
for _ in range(100):
    # mid - длина куска
    mid = (l + r) / 2
    if ok(ropes, k, mid):
        ans = mid
        l = mid
    else:
        r = mid
print(mid)
