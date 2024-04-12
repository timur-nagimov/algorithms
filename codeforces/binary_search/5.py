'https://codeforces.com/edu/course/2/lesson/6/2/practice/contest/283932/problem/A'


def ok(w, h, n, mid):
    # mid - сторона квадрата
    return (mid//w)*(mid//h) >= n


w, h, n = map(int, input().split())
l = 0
r = 10**18
ans = -1
while l <= r:
    mid = (l+r)//2
    if ok(w, h, n, mid):
        r = mid - 1
        ans = mid
    else:
        l = mid + 1
print(ans)
