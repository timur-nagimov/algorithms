class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        pref_sum = [0]*(n+1)
        for i in range(n):
            pref_sum[i+1] = pref_sum[i] + gain[i]

        return max(pref_sum)
