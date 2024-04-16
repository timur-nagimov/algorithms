# https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


p1 = 0
p2 = 0

ans = []
while p1 < len(a) or p2 < len(b):
    if p1 == len(a):
        ans.append(b[p2])
        p2 += 1
    elif p2 == len(b):
        ans.append(a[p1])
        p1 += 1
    else:
        if a[p1] < b[p2]:
            ans.append(a[p1])
            p1 += 1
        else:
            ans.append(b[p2])
            p2 += 1

print(' '.join(map(str, ans)))
