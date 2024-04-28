class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1

        max_ans = 0
        while l < r:
            cur_min_border = min(height[l], height[r])
            cur_max_ans = cur_min_border*(r-l)
            max_ans = max(max_ans, cur_max_ans)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_ans
