class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pref_sums = [0]*(n+1)
        for i in range(n):
            pref_sums[i+1] = pref_sums[i] + nums[i]

        prev_dict = {}
        ans = 0
        for i in pref_sums:
            if i % k in prev_dict:
                ans += prev_dict[i % k]

            prev_dict[i % k] = prev_dict.get(i % k, 0) + 1

        return ans
