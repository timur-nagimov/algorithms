class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict_nums = {}
        for num in nums:
            dict_nums[num] = dict_nums.get(num, 0) + 1

        for value in dict_nums.values():
            if value > 1:
                return True
        return False
