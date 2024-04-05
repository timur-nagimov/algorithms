n1 = int(input())
set1 = set(map(int, input().split()))

n2 = int(input())
set2 = set(map(int, input().split()))

n3 = int(input())
set3 = set(map(int, input().split()))


final_set = set1.intersection(
    set2) | set1.intersection(set3) | set2.intersection(set3)


print(' '.join(map(str, sorted(final_set))))
