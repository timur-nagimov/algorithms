def binary_search(arr, n, target, find_first):
    left = 0
    right = N-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            if find_first:
                right = mid - 1
            else:
                left = mid + 1
    return left if find_first else right


N = int(input())
arr = sorted(list(map(int, input().split())))
K = int(input())
answers = []
for _ in range(K):
    L, R = map(int, input().split())
    l_index = binary_search(arr, N, L, True)
    r_index = binary_search(arr, N, R, False)
    answers.append(r_index - l_index + 1)

print(' '.join(map(str, answers)))
