n = int(input())
arr = list(map(int, input().split()))

pref_sums = [0]*(n+1)
for i in range(n):
    # след.ячейка = предыдущая + значение текущего элемента списка
    pref_sums[i+1] = pref_sums[i] + arr[i]

print(pref_sums)
