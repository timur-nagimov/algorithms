# https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/C

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = 0
j = 0

ans = 0
answers = [0]*n
while i < n:

    while j < m and b[j] <= a[i]:
        if a[i] == b[j]:
            answers[i] += 1
        j += 1

    if i != 0 and a[i] == a[i-1]:
        answers[i] = answers[i-1]
    i += 1

print(sum(answers))
