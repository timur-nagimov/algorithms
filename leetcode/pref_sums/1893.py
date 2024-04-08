class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        pref_sums = [0]*(53)

        for x1, x2 in ranges:
            pref_sums[x1] += 1
            pref_sums[x2 + 1] += -1

        for i in range(52):
            pref_sums[i+1] += pref_sums[i]

        for i in range(left, right+1):
            if pref_sums[i] == 0:
                return False
        return True
