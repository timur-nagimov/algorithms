class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        new_point = intervals[0]

        answer = []
        for i in range(len(intervals)):
            if new_point[1] >= intervals[i][0]:
                new_point = [new_point[0], max(new_point[1], intervals[i][1])]
            else:
                answer.append(new_point)
                new_point = intervals[i]

        answer.append(new_point)
        return answer
