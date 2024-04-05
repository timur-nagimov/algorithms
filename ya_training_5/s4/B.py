# if first right - 1
# if last left + 1

def get_number_by_k(k):
    return k*k*(k+1)//2 - (k-1)*k*(k+1)//3 + k*(k+1)//2 - 1


def binary_search(number):
    if number == 1:
        return 1
    l = 0
    r = number
    while l < r:
        middle = (l+r+1)//2
        if get_number_by_k(middle) > number:
            r = middle - 1
        else:
            l = middle
    return l


number = int(input())
print(binary_search(number))
