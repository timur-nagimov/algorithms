class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0:
            return []
        l = 0
        r = 0

        answer = []
        while r < n - 1:
            if nums[r] + 1 != nums[r+1]:
                if l != r:
                    answer.append(f'{nums[l]}->{nums[r]}')
                else:
                    answer.append(str(nums[r]))
                l = r + 1
            r += 1
        # добавляем конец
        if l == r:
            answer.append(str(nums[r]))
        else:
            answer.append(f'{nums[l]}->{nums[r]}')

        return answer
