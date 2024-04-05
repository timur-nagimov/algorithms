def binary_search(prefix_sum, n, m, rota_count, total_number):
    l = 0
    r = n-rota_count+1

    while l < r-1:
        m = (l + r)//2
        if prefix_sum[m+rota_count] - prefix_sum[m] > total_number:
            r = m
        else:
            l = m
    answer = l + 1 if prefix_sum[l+rota_count] - \
        prefix_sum[l] == total_number else -1
    return answer


n, m = map(int, input().split())
numbers = list(map(int, input().split()))

prefix_sum = [0]
for i in range(n):
    prefix_sum.append(prefix_sum[i]+numbers[i])

answers = []
for i in range(m):
    rota_count, total_number = map(int, input().split())
    answer = binary_search(prefix_sum, n, m, rota_count, total_number)
    answers.append(answer)


for ans in answers:
    print(ans)
