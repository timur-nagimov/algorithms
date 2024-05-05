class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        cur_changes = k

        l = 0
        answer = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                cur_changes -= 1
            if cur_changes >= 0:
                answer = max(answer, r-l+1)

            while cur_changes < 0:
                if nums[l] == 0:
                    cur_changes += 1
                l += 1

        return answer
