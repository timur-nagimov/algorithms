'https://codeforces.com/edu/course/2/lesson/6/1/practice/contest/283911/problem/B'
# Ближайшее слева (макс.слева не больше данного)

n, k = map(int, input().split())
arr = list(map(int, input().split()))
search_nums = list(map(int, input().split()))


def ok(arr, num, mid):
    return arr[mid] <= num


for num in search_nums:
    l = 0
    r = n - 1
    ans = -1
    while l <= r:
        mid = (l+r)//2
        if ok(arr, num, mid):
            l = mid + 1
            ans = mid
        else:
            r = mid - 1
    print(ans+1)
