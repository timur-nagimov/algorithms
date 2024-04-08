class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        pref_sum = [0]*(n+1)
        for i in range(n):
            pref_sum[i+1] = pref_sum[i] + nums[i]

        suf_sum = [0]*(n+1)
        for i in range(n-1, -1, -1):
            suf_sum[i] = suf_sum[i+1] + nums[i]

        for i in range(n):
            if pref_sum[i] == suf_sum[i] - nums[i]:
                return i
        return -1
