p, v = list(map(int, input().split()))
q, m = list(map(int, input().split()))

max_trees = 2*(v + m + 1)
left_tree_bound = min(p+v, q+m)
right_tree_bound = max(q-m, p-v)

# если < 0, то все разграничено
answer = max_trees - max(0, left_tree_bound-right_tree_bound + 1)

print(answer)
