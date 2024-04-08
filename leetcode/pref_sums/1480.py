class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref_sums = [0]*(n+1)
        for i in range(n):
            pref_sums[i+1] = pref_sums[i] + nums[i]

        return pref_sums[1:]
