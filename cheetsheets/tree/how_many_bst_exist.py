# Через числа Каталана выражается то, сколько существует бин.деревьев поиска с возможными значениями в вершинах от 1 до n
# Само число Каталана выражается формулой C(n) = (2n)!/n!(n+1)!

def catalan_numbers(n: int):
    catalan_list = [1]

    for i in range(1, n):
        catalan_list.append(0)
        for j in range(0, i):
            catalan_list[i] += catalan_list[j] * catalan_list[i-j-1]

    return catalan_list[n-1]


n = int(input()) + 1
print(catalan_numbers(n))
