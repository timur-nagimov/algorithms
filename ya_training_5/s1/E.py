# import sys

# sys.set_int_max_str_digits(999999999)

n, k, d = list(map(int, input().split()))
n = str(n)


def main(n, k, d):
    for current_step in range(d):
        current_mod = int(n) % k
        is_added = False
        for symbol in range(10):
            if (current_mod*10 + symbol) % k == 0:
                if symbol == 0:
                    n = f'{n}{str(symbol)* (d - current_step)}'
                    return n
                n += str(symbol)
                is_added = True
                break
        if not is_added:
            return -1
    return n


print(main(n, k, d))
