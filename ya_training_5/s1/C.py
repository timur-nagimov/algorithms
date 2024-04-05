def get_spacebar_compatibility(space_number: int) -> int:
    main_part = space_number // 4
    secondary_part = space_number % 4
    operation_numbers = 2 if secondary_part == 3 else secondary_part

    operation_numbers += main_part
    return operation_numbers


n = int(input())
ans = 0
for _ in range(n):
    ans += get_spacebar_compatibility(int(input()))

print(ans)
