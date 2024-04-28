class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        left_stack = [(-1, -1)]
        left = [0]*n
        for i in range(n):
            while heights[i] < left_stack[-1][0]:
                left_stack.pop()
            left[i] = left_stack[-1][1]
            left_stack.append((heights[i], i))

        right_stack = [(-1, n)]
        right = [0]*n
        for i in range(n-1, -1, -1):
            while heights[i] <= right_stack[-1][0]:
                right_stack.pop()
            right[i] = right_stack[-1][1]
            right_stack.append((heights[i], i))

        max_ans = 0
        for i in range(n):
            max_ans = max(max_ans, heights[i]*(right[i]-left[i] - 1))

        return max_ans
