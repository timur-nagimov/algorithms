# https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# для каждого числа из b найти количество чисел
# из первого массива, которые меньше числа из b

p1 = 0
p2 = 0
ans = []

while p2 < len(b):
    cnt = 0
    while p1 < len(a) and b[p2] > a[p1]:
        cnt += 1
        p1 += 1

    if p2 == 0:
        ans.append(cnt)
    else:
        ans.append(ans[-1] + cnt)
    p2 += 1

print(' '.join(map(str, ans)))
