"""https://contest.yandex.ru/contest/27393/problems/C/"""


def del_sybmols(number: str):
    number = number.replace('+', '')
    number = number.replace('(', '')
    number = number.replace(')', '')
    number = number.replace('-', '')
    start_index = 1
    if len(number) == 7 or len(number) == 10:
        start_index = 0

    number = f'7{number[start_index:]}'
    if len(number) != 11:
        number = f'{number[0]}495{number[1:]}'
    return number


def main():
    a = del_sybmols(input())
    b = del_sybmols(input())
    c = del_sybmols(input())
    d = del_sybmols(input())
    if a == b:
        print('YES')
    else:
        print('NO')

    if a == c:
        print('YES')
    else:
        print('NO')

    if a == d:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
