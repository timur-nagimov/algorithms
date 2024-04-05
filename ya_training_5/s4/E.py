def bin_search(n):
    l, r = 0, n
    while l < r:
        m = (l + r) // 2
        if m * (m + 1) // 2 < n:
            l = m + 1
        else:
            r = m
    return l


def f_seq(n):
    l = bin_search(n)
    ds = l + 1
    pds = (l - 1) * l // 2
    num = n - pds if l % 2 else ds - (n - pds)
    den = ds - num if l % 2 else n - pds

    return num, den


n = int(input())
ans = f_seq(n)
print(f'{ans[0]}/{ans[1]}')
