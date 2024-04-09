class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pref_sum = [0]*n
        pref_sum[0] = nums[0]
        for i in range(1, n):
            pref_sum[i] = pref_sum[i-1] | nums[i]

        suf_sum = [0]*n
        suf_sum[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            suf_sum[i] = suf_sum[i+1] | nums[i]

        max_ans = 0
        for i in range(n):
            num = nums[i] * (1 << k)
            if i - 1 >= 0:
                num = pref_sum[i-1] | num
            if i + 1 < n:
                num = num | suf_sum[i+1]
            max_ans = max(max_ans, num)
        return max_ans
