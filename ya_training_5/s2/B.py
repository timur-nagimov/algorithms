n, k = map(int, input().split())
days_price = list(map(int, input().split()))


best_profit = 0
for i in range(len(days_price)):
    current_profit = 0 - days_price[i]
    for j in range(1, k+1):
        if i + j >= len(days_price):
            break
        if current_profit + days_price[i+j] > best_profit:
            best_profit = current_profit + days_price[i+j]


print(best_profit)
