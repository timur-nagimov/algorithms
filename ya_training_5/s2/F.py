def main():
    n = int(input())
    segments = list(map(int, input().split()))
    a, b, k = map(int, input().split())

    optimal = -1

    min_wheel = (a - 1) // k
    max_wheel = min_wheel + n - \
        1 if (b - 1) // k - min_wheel >= n - 1 else (b - 1) // k

    for i in range(min_wheel, max_wheel + 1):
        first_try = max(optimal, segments[i % n])
        optimal = max(first_try, segments[n - (n + i - 1) % n - 1])

    print(optimal)


if __name__ == '__main__':
    main()
