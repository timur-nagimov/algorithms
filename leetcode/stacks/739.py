class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0]*n
        stack = [(temperatures[0], 0),]

        for i in range(1, n):
            while stack and temperatures[i] > stack[-1][0]:
                val = stack.pop()
                answer[val[1]] = i - val[1]
            stack.append((temperatures[i], i))
        return answer
