class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numbers = set(nums)

        numbers_dict = {}
        max_ans = 1
        for num in numbers:
            prev_num = numbers_dict.get(num-1, 0)
            next_num = numbers_dict.get(num+1, 0)

            summa = prev_num + next_num + 1
            numbers_dict[num-prev_num] = summa
            numbers_dict[num+next_num] = summa
            max_ans = max(max_ans, summa)

        return max_ans
