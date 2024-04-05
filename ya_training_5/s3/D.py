n, k = map(int, input().split())
numbers = list(map(int, input().split()))

ans = 'NO'
numbers_dict = {}

for i in range(n):
    numbers_dict[numbers[i]] = numbers_dict.get(numbers[i], [])
    numbers_dict[numbers[i]].append(i)


for key, value in numbers_dict.items():
    for i in range(len(value)-1):
        if abs(value[i] - value[i+1]) <= k:
            ans = 'YES'
            break

print(ans)
