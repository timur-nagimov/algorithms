# https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

# Число меньших (для каждого элемента второго массива найти число меньших в первом)
# Массивы отсортированы по неубыванию

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans_arr = []

p1 = 0
p2 = 0

cnt_lower = 0
while p2 < m:

    while p1 < n and b[p2] > a[p1]:
        cnt_lower += 1
        p1 += 1

    ans_arr.append(cnt_lower)
    p2 += 1

print(' '.join(map(str, ans_arr)))
