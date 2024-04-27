class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref_mult = [1]*(n+1)
        pref_mult[1] = nums[0]
        for i in range(1, n):
            pref_mult[i+1] = pref_mult[i] * nums[i]

        suf_mult = [1]*(n+1)
        suf_mult[n-1] = nums[n-1]
        for i in range(n-1, 0, -1):
            suf_mult[i-1] = suf_mult[i]*nums[i-1]

        ans = []
        for i in range(1, n+1):
            ans.append(suf_mult[i]*pref_mult[i-1])

        return ans
