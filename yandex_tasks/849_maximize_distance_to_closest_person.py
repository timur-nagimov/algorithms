class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        pref_dist = [0]*(n + 1)
        suf_dist = [0]*(n + 1)

        for i in range(n):
            if seats[i] == 0:
                # i + 1 - сколько свободных мест слева для i
                pref_dist[i+1] = pref_dist[i] + 1

        for i in range(n-1, -1, -1):
            if seats[i] == 0:
                # i - сколько свободных мест справа для i
                suf_dist[i] = suf_dist[i + 1] + 1

        # Изначально задаем максимуму значение на границах:
        # сколько свободных мест слева для послед. сиденья
        # и сколько свободных мест справа для первого сиденья
        max_ans = max(pref_dist[n], suf_dist[0])
        for i in range(n):
            if seats[i] == 0:
                max_ans = max(max_ans, min(pref_dist[i + 1], suf_dist[i]))

        return max_ans
