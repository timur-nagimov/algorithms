import sys


def calc_min_max_optimized(y, h):
    n = len(y)
    pref_min, pref_max = [0] * n, [0] * n
    suf_min, suf_max = [0] * n, [0] * n

    pref_min[0], pref_max[0] = y[0], y[0]
    for i in range(1, n):
        pref_min[i] = min(pref_min[i - 1], y[i])
        pref_max[i] = max(pref_max[i - 1], y[i])

    suf_min[n-1], suf_max[n-1] = y[n-1], y[n-1]
    for i in range(n - 2, -1, -1):
        suf_min[i] = min(suf_min[i + 1], y[i])
        suf_max[i] = max(suf_max[i + 1], y[i])

    return pref_min, pref_max, suf_min, suf_max


def main():
    readline = sys.stdin.readline
    w, h, n = map(int, readline().split())
    p = [tuple(map(int, readline().split())) for _ in range(n)]

    p.sort()

    y = [p[i][1] for i in range(n)]

    pref_min_y, pref_max_y, suf_min_y, suf_max_y = calc_min_max_optimized(y, h)

    cl, cr = 1, min(w, h)
    while cl < cr:
        mid = (cl + cr) // 2
        l = 0
        for r in range(n):
            while p[r][0] - p[l][0] >= mid:
                l += 1

            max_y = max(pref_max_y[l - 1] if l > 0 else -1,
                        suf_max_y[r + 1] if r + 1 < n else -1)
            min_y = min(pref_min_y[l - 1] if l > 0 else h + 1,
                        suf_min_y[r + 1] if r + 1 < n else h + 1)

            if min_y == -1 or max_y - min_y + 1 <= mid:
                cr = mid
                break
        else:
            cl = mid + 1

    return cl


if __name__ == "__main__":
    sys.stdout.write(f"{main()}\n")
