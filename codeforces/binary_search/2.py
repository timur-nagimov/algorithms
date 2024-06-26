n, k = map(int, input().split())
arr = list(map(int, input().split()))
find_numbs = map(int, input().split())


def ok(arr, numb, mid):
    return arr[mid] <= numb


for numb in find_numbs:
    l = 0
    r = n-1
    ans = -1
    while l <= r:
        mid = (l+r) // 2
        if ok(arr, numb, mid):
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    print(ans+1)
