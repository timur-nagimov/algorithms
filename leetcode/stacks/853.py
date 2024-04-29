class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        stack = []
        cars_info = []

        for i in range(n):
            cars_info.append((position[i], speed[i]))

        cars_info.sort(reverse=True)
        for i in range(n):
            cur_time = (target - cars_info[i][0]) / cars_info[i][1]

            stack.append(cur_time)
            # чем больше cur_time - тем больше ехать
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
