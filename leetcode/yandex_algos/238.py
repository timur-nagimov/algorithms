class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        # вывести минимальное кол-во диапазонов, куда входят все числа
        answer = []
        l = nums[0]
        r = None

        for i in range(1, len(nums)):
            if l + 1 == nums[i] or (r is not None and r + 1 == nums[i]):
                r = nums[i]
            else:
                if r is None:
                    answer.append(f'{l}')
                else:
                    answer.append(f'{l}->{r}')
                l = nums[i]
                r = None

        if r is None:
            answer.append(f'{l}')
        else:
            answer.append(f'{l}->{r}')
        return answer
