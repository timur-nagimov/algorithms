class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def get_pairs(n, answer, left_count=0, right_count=0, cur=''):
            if left_count + right_count == 2*n:
                answer.append(cur)
                return

            if left_count < n:
                get_pairs(n, answer, left_count+1, right_count, cur+'(')
            if right_count < left_count:
                get_pairs(n, answer, left_count, right_count+1, cur+')')

        answer = []
        get_pairs(n, answer)
        return answer
