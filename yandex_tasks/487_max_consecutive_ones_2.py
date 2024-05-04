class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        zero_pos = 0
        can_change = True

        ans = 0
        for r in range(len(nums)):
            if nums[r] == 0 and can_change:
                can_change = False
                zero_pos = r
                ans = max(ans, r-l+1)
            elif nums[r] == 1:
                ans = max(ans, r-l+1)
            else:
                l = zero_pos + 1
                zero_pos = r
        return ans
