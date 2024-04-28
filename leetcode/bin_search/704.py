class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        n = len(nums)

        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        if l < n and nums[l] == target:
            return l
        return -1