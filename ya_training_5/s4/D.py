def find_min_number_of_rows(w, a, b):
    l, r = 0, w
    ans = float('inf')
    while l < r - 1:
        m = (l + r) // 2
        rows_a = rows_b = 1
        width_a = width_b = 0

        for ai in a:
            if ai > m:
                rows_a = float('inf')
                break
            if width_a + ai > m:
                rows_a += 1
                width_a = 0
            width_a += ai + 1

        for bi in b:
            if bi > w - m:
                rows_b = float('inf')
                break
            if width_b + bi > w - m:
                rows_b += 1
                width_b = 0
            width_b += bi + 1

        max_rows = max(rows_a, rows_b)
        ans = min(ans, max_rows)

        if rows_a < rows_b:
            r = m
        else:
            l = m

    return ans


def main():
    w, n, m = map(int, input().split())
    f_arr = list(map(int, input().split()))
    s_arr = list(map(int, input().split()))

    print(find_min_number_of_rows(w, f_arr, s_arr))


if __name__ == '__main__':
    main()
