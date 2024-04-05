n = int(input())
line_parts = list(map(int, input().split()))

max_part = 0
parts_sum = 0
for line in line_parts:
    if line > max_part:
        max_part = line

    parts_sum += line


parts_sum -= max_part
if max_part > parts_sum:
    print(max_part - parts_sum)
else:
    print(parts_sum + max_part)
