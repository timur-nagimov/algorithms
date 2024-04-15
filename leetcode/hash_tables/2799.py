class Solution:
    """Not optimnal solution."""

    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        k = len(set(nums))
        ans = 0
        for i in range(n):
            numbers_set = set()
            for j in range(i, n):
                numbers_set.add(nums[j])

                if len(numbers_set) >= k:
                    ans += 1
        return ans
