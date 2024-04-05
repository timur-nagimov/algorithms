def get_dist(x, y, target_x, target_y):
    return abs(target_x-x) + abs(target_y - y)


def minimum(y, N, ships):
    my_ships = ships.copy()
    cur_distance = 0
    for x in range(N):
        target_x, target_y = my_ships.pop()
        cur_distance += get_dist(x, y, target_x, target_y)
    return cur_distance


def calculate(ships, N):

    answer = 10**9 + 1
    for y in range(N):
        answer = min(minimum(y, N, ships), answer)

    return answer


def main():
    N = int(input())
    ships = []
    for _ in range(N):
        x, y = map(int, input().split())
        ships.append([x-1, y-1])
    ships.sort(reverse=True)
    print(calculate(ships, N))


if __name__ == '__main__':
    main()
