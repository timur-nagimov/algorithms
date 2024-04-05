def is_anagrams(str1, str2):
    if len(str1) != len(str2):
        return "NO"

    count_str1 = {}
    count_str2 = {}

    for symbol in str1:
        count_str1[symbol] = count_str1.get(symbol, 0) + 1
    for symbol in str2:
        count_str2[symbol] = count_str2.get(symbol, 0) + 1

    if count_str1 == count_str2:  # noqa: R505
        return "YES"
    else:
        return "NO"


# Чтение входных данных
str1 = input()
str2 = input()

# Вывод результата
print(is_anagrams(str1, str2))
