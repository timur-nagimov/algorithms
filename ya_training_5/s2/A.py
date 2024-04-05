n = int(input())

max_x = max_y = -1
min_x = min_y = 10**9 + 1

for _ in range(n):
    x, y = map(int, input().split())
    if x > max_x:
        max_x = x
    if x < min_x:
        min_x = x

    if y > max_y:
        max_y = y
    if y < min_y:
        min_y = y

print(min_x, min_y, max_x, max_y)
