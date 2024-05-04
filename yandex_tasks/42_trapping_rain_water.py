class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        l_max = 0
        r_max = 0

        answer = 0
        while l <= r:

            # двигаем ту сторону, где максимум - меньше
            # ту сторону которую двинул - записываю значение
            if l_max > r_max:
                answer += max(0, min(l_max, r_max) - height[r])
                r_max = max(r_max, height[r])
                r -= 1
            else:
                answer += max(0, min(l_max, r_max) - height[l])
                l_max = max(l_max, height[l])
                l += 1
        return answer
