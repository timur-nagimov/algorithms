class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        # по списку, добавляем первые k элементов в словарь где ключи - их кол-во
        # если количество ключей >= m, то сохраняем в max_sum = max(sum(cur_arr, max_sum))
        # на следующих итерациях делаем минус значения от предыдущего, если ключ обнулился дропаем его
        # также добавляем новый ключ или прибавляем значение если он существует
        max_ans = 0
        n = len(nums)

        nums_dict = {}
        tmp_sum = 0
        for number in nums[0:k]:
            nums_dict[number] = nums_dict.get(number, 0) + 1
            tmp_sum += number
        if len(nums_dict.keys()) >= m:
            max_ans = tmp_sum

        for i in range(k, n):
            tmp_sum -= nums[i - k]
            tmp_sum += nums[i]

            nums_dict[nums[i - k]] -= 1
            if nums_dict[nums[i - k]] <= 0:
                del nums_dict[nums[i - k]]
            nums_dict[nums[i]] = nums_dict.get(nums[i], 0) + 1

            if len(nums_dict.keys()) >= m:
                max_ans = max(tmp_sum, max_ans)

        return max_ans
