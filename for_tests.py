import heapq

heap = [1, 2, 5486, -1, 2, 0, 1, 1, 1]

heapq.heapify(heap)
print(heap)

while heap:
    print(heapq.heappop(heap))
