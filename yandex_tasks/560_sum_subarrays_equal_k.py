class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref_sum = 0
        prev_sums = {}
        prev_sums[pref_sum] = 1
        # можно решить за O(n^2) полным перебором без исп. доп памяти
        answer = 0
        for i in range(len(nums)):
            pref_sum += nums[i]
            answer += prev_sums.get(pref_sum-k, 0)

            prev_sums[pref_sum] = prev_sums.get(pref_sum, 0) + 1

        return answer
