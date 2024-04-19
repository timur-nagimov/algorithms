# https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/C

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Число пар равных чисел
i = 0
j = 0

ans_arr = [0]*m
while j < m:

    while i < n and a[i] <= b[j]:
        if a[i] == b[j]:
            ans_arr[j] += 1
            i += 1

    if j > 0 and b[j-1] == b[j]:
        ans_arr[j] = ans_arr[j-1]

    j += 1


print(sum(ans_arr))
