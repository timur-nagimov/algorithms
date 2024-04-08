class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref_sum = [0]*(n+1)
        for i in range(n):
            pref_sum[i+1] = pref_sum[i] + nums[i]

        suf_sum = [0]*(n+1)
        for i in range(n, 0, -1):
            suf_sum[i-1] = suf_sum[i] + nums[i-1]

        ans = []
        for i in range(n):
            ans.append(abs(pref_sum[i+1] - suf_sum[i]))
        return ans
