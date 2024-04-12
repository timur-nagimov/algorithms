# https://codeforces.com/edu/course/2/lesson/6/1/practice/contest/283911/problem/A
# Вывести YES - если число есть в списке, иначе вывести NO
def ok(numbers, find_numb, mid):
    return numbers[mid] <= find_numb


n, k = map(int, input().split())
numbers = list(map(int, input().split()))
find_numbs = list(map(int, input().split()))


for find_numb in find_numbs:
    ans = -1
    l = 0
    r = n - 1
    while l <= r:
        mid = (l + r) // 2
        if ok(numbers, find_numb, mid):
            ans = mid
            l = mid + 1
        else:
            r = mid - 1

    if ans != -1 and numbers[ans] == find_numb:
        print('YES')
    else:
        print('NO')
