class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        pref_sum = nums.copy()
        suf_sum = nums.copy()

        for i in range(1, n):
            if pref_sum[i] == 0:
                continue
            pref_sum[i] += pref_sum[i-1]
            ans = 1
        for i in range(n-2, -1, -1):
            if suf_sum[i] == 0:
                continue
            suf_sum[i] += suf_sum[i+1]

        ans = max(pref_sum[0], suf_sum[-1])
        for i in range(1, n-1):
            ans = max(ans, pref_sum[i-1]+suf_sum[i+1])
            ans = max(ans, pref_sum[i], suf_sum[i])

        return ans
