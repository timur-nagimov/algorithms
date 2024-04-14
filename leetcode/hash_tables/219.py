class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        nums_dict = {}
        move_k = k
        for i in range(len(nums)):
            if nums[i] in nums_dict:
                return True
            if move_k > 0:
                nums_dict[nums[i]] = nums_dict.get(nums[i], 0) + 1
                move_k -= 1
            else:
                nums_dict[nums[i-k]] -= 1
                if nums_dict[nums[i-k]] == 0:
                    del nums_dict[nums[i-k]]
                nums_dict[nums[i]] = nums_dict.get(nums[i], 0) + 1

        return False
