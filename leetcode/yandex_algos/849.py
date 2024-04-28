class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        left_neighbors_distances = [None]*n
        right_neighbors_distances = [None]*n

        for i in range(0, n):
            if seats[i] == 1:
                left_neighbors_distances[i] = 0
            elif i != 0:
                if left_neighbors_distances[i-1] is not None:
                    left_neighbors_distances[i] = left_neighbors_distances[i-1] + 1

        for i in range(n-1, -1, -1):
            if seats[i] == 1:
                right_neighbors_distances[i] = 0
            elif i != n-1:
                if right_neighbors_distances[i+1] is not None:
                    right_neighbors_distances[i] = right_neighbors_distances[i+1] + 1

        max_ans = 0
        for i in range(n):
            if right_neighbors_distances[i] is None:
                max_ans = max(max_ans, left_neighbors_distances[i])
            elif left_neighbors_distances[i] is None:
                max_ans = max(max_ans, right_neighbors_distances[i])
            else:
                max_ans = max(max_ans, min(
                    left_neighbors_distances[i], right_neighbors_distances[i]))

        return max_ans
