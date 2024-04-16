# https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

n, s = map(int, input().split())
arr = list(map(int, input().split()))

l = 0
r = 0
cur_sum = 0
answer = float('inf')
answer_exist = False

while l < n:
    while r < n and cur_sum < s:
        cur_sum += arr[r]
        r += 1

    if cur_sum >= s:
        answer_exist = True
        answer = min(answer, r - l)

    cur_sum -= arr[l]
    l += 1

if answer_exist:
    print(answer)
else:
    print(-1)
