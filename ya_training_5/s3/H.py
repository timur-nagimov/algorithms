def main():
    n = int(input())
    original = []
    transformed = []
    max_matches = 0

    for i in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        if x1 > x2 or (x1 == x2 and y1 > y2):
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        original.append((x1, y1, x2, y2))

    for i in range(n):
        xx1, yy1, xx2, yy2 = map(int, input().split())
        if xx1 > xx2 or (xx1 == xx2 and yy1 > yy2):
            xx1, xx2 = xx2, xx1
            yy1, yy2 = yy2, yy1
        transformed.append((xx1, yy1, xx2, yy2))

    transformations = {}

    for i in range(n):
        for j in range(n):
            dx = transformed[j][0] - original[i][0]
            dy = transformed[j][1] - original[i][1]

            if original[i][2] + dx != transformed[j][2] or original[i][3] + dy != transformed[j][3]:
                continue

            transformation = (dx, dy)
            transformations[transformation] = transformations.get(
                transformation, 0) + 1

            max_matches = max(max_matches, transformations[transformation])

    print(n - max_matches)


if __name__ == "__main__":
    main()
