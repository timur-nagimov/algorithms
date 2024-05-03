class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first_cur = 0
        second_cur = 0

        answer = []
        while first_cur < len(firstList) and second_cur < len(secondList):
            x1, y1 = firstList[first_cur]
            x2, y2 = secondList[second_cur]

            ans_x = max(x1, x2)
            ans_y = min(y1, y2)

            if ans_x <= ans_y:
                answer.append([ans_x, ans_y])

            if y1 > y2:
                second_cur += 1
            else:
                first_cur += 1

        return answer
