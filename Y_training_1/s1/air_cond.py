"""https://contest.yandex.ru/contest/27393/problems/A/"""


def main():
    t_room, t_cond = list(map(int, input().split()))
    mode = input()
    if t_room >= t_cond:
        if mode == 'heat':
            return t_room
        if mode == 'freeze':
            return t_cond
        if mode == 'fan':
            return t_room
        return t_cond
    if t_room < t_cond:
        if mode == 'heat':
            return t_cond
        if mode == 'freeze':
            return t_room
        if mode == 'fan':
            return t_room
        return t_cond

    return 'miss'


if __name__ == '__main__':
    print(main())
