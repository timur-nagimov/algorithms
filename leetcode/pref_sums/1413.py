class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        pref_sum = [0]*(n+1)

        for i in range(n):
            pref_sum[i+1] = pref_sum[i] + nums[i]

        min_el = min(pref_sum)
        if min_el < 1:
            return 1 + abs(min_el)
        return 1
