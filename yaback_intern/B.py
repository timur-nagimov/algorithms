def bin_search(words, prefix, k):
    l = 0
    r = len(words) - 1
    start = -1

    while l <= r:
        mid = (l + r) // 2
        if words[mid].startswith(prefix):
            start = mid
            r = mid - 1
        elif words[mid] < prefix:
            l = mid + 1
        else:
            r = mid - 1

    if start == -1:
        return -1

    if start + k - 1 < len(words) and words[start + k - 1].startswith(prefix):
        return start + k
    else:
        return -1


n, q = map(int, input().split())
words = []
for _ in range(n):
    words.append(input())
for _ in range(q):
    k, prefix = input().split()
    k = int(k)
    print(bin_search(words, prefix, k))
