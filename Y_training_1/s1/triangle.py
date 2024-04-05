"""https://contest.yandex.ru/contest/27393/problems/B/"""


def main():
    a = int(input())
    b = int(input())
    c = int(input())

    if a + b <= c or a + c <= b or b + c <= a:
        print('NO')
    else:
        print('YES')


if __name__ == '__main__':
    main()
