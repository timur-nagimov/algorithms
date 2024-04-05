n = int(input())
numbers = list(map(int, input().split()))

numbers_dict = {}
for number in numbers:
    numbers_dict[number] = numbers_dict.get(number, 0) + 1

min_numb = 0

for numb, count in numbers_dict.items():
    min_numb = max(count + numbers_dict.get(numb+1, 0), min_numb)

print(n - min_numb)
