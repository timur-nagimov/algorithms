from itertools import combinations


def main():
    N = int(input())

    points = set()
    for i in range(N):
        points.add(tuple(map(int, input().split())))

    def find_missing_square_vertices(x1, y1, x2, y2):
        xc = (x1 + x2) / 2
        yc = (y1 + y2) / 2
        xd = (x1 - x2) / 2
        yd = (y1 - y2) / 2

        x3 = xc - yd
        y3 = yc + xd
        x4 = xc + yd
        y4 = yc - xd

        # Проверка на целочисленность координат
        if x3.is_integer():
            return (int(x3), int(y3)), (int(x4), int(y4))
        else:
            return None, None

    min_len = float('inf')
    candidates = []
    for point1, point2 in combinations(points, 2):
        x1, y1 = point1
        x2, y2 = point2

        new1, new2 = find_missing_square_vertices(x1, y1, x2, y2)
        if new1 is None:
            continue
        potential_points = [new1, new2]
        potential_len = 2
        if new1 in points:
            potential_points.remove(new1)
            potential_len -= 1
        if new2 in points:
            potential_points.remove(new2)
            potential_len -= 1

        if min_len > potential_len:
            min_len = potential_len
            candidates = potential_points
            if min_len == 0:
                break

    if N == 1:
        min_len = 3
        for point in points:
            x, y = point
            candidates = [(x+1, y), (x, y+1), (x+1, y+1)]
    print(min_len)
    for point in candidates:
        print(point[0], point[1])


if __name__ == '__main__':
    main()
