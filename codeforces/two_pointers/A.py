# https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


p1 = 0
p2 = 0

ans_arr = []
while p1 < n or p2 < m:
    if p1 == n:
        ans_arr.append(b[p2])
        p2 += 1
    elif p2 == m:
        ans_arr.append(a[p1])
        p1 += 1
    else:
        if a[p1] > b[p2]:
            ans_arr.append(b[p2])
            p2 += 1
        else:
            ans_arr.append(a[p1])
            p1 += 1

print(' '.join(map(str, ans_arr)))
