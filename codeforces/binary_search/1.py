n, k = map(int, input().split())
numbers = list(map(int, input().split()))
queries = list(map(int, input().split()))


def ok(numbers, query, mid):
    return numbers[mid] <= query


for query in queries:
    ans =
    l = 0
    r = n - 1  # index
    while l <= r:
        mid = (l + r) // 2
        if ok(numbers, query, mid):
            ans = numbers[mid]
            l = mid + 1
        else:
            r = mid - 1

    if ans == query:
        print('YES')
    else:
        print('NO')
