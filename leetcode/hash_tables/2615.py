class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        right_dict = {}
        # суммы справа
        for i in range(n):
            num = nums[i]
            if num in right_dict:
                right_dict[num][0] += i
                right_dict[num][1] += 1
            else:
                right_dict[num] = [i, 1]

        ans_numbers = [0]*n
        left_dict = {}
        # подсчет ответа + суммы слева
        for i in range(n):
            num = nums[i]
            # дропаем текущий элемент из right_dict
            right_dict[num][0] -= i
            right_dict[num][1] -= 1

            tmp_ans = 0
            tmp_ans += right_dict[num][0] - i*right_dict[num][1]
            print(tmp_ans)

            # считаем left_dict
            if num in left_dict:
                tmp_ans += i*left_dict[num][1] - left_dict[num][0]
                left_dict[num][0] += i
                left_dict[num][1] += 1
            else:
                left_dict[num] = [i, 1]

            ans_numbers[i] = tmp_ans

        return ans_numbers
