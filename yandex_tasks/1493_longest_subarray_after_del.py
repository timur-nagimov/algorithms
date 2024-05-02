class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        pref_sum = [0]*(n + 1)
        suf_sum = [0]*(n + 1)

        for i in range(n):
            if nums[i] == 1:
                pref_sum[i+1] = pref_sum[i] + nums[i]
        for i in range(n - 1, -1, -1):
            if nums[i] == 1:
                suf_sum[i] = suf_sum[i + 1] + nums[i]

        max_ans = 0
        print(pref_sum)
        print(suf_sum)
        for i in range(n):
            max_ans = max(max_ans, pref_sum[i] + suf_sum[i+1])

        return max_ans
