class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = c = len(nums) - 1

        answer = [0]*len(nums)
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                answer[c] = nums[l]**2
                l += 1
            else:
                answer[c] = nums[r]**2
                r -= 1
            c -= 1

        return answer
