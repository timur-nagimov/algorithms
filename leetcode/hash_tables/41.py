class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_dict = {}
        for num in nums:
            num_dict[num] = True

        for i in range(1, 2**17):
            if i not in num_dict:
                return i
