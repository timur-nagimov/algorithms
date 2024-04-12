'https://codeforces.com/edu/course/2/lesson/6/1/practice/contest/283911/problem/D'


n = int(input())
arr = list(map(int, input().split()))
arr.sort()
k = int(input())

pairs = []
for _ in range(k):
    l, r = map(int, input().split())
    pairs.append((l, r))

answers = []
for pair in pairs:
    l = 0
    r = n - 1
    left_index = 0
    right_index = 0
    # ищем левую границу
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] >= pair[0]:
            r = mid - 1
            left_index = mid
        else:
            l = mid + 1
    l = 0
    r = n - 1
    # ищем правую границу
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] <= pair[1]:
            l = mid + 1
            right_index = mid
        else:
            r = mid - 1
    if arr[left_index] < pair[0] or arr[right_index] > pair[1]:
        answers.append(0)
    else:
        answers.append(right_index-left_index+1)

print(' '.join(map(str, answers)))
