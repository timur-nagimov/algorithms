n = int(input())
numbers = list(map(int, input().split()))

ans = ''

prev_all = numbers[0] % 2
# надо получить знаки для получения нечетного числа
for number in numbers[1:]:
    if (prev_all * number) % 2 == 1:
        prev_all *= number % 2
        ans = f'{ans}x'
    else:
        prev_all += number % 2
        ans = f'{ans}+'


print(ans)
