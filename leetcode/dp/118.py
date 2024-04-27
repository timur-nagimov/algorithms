class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[0]*numRows for _ in range(numRows)]
        for i in range(numRows):
            dp[i][i] = 1
            dp[i][0] = 1

        for i in range(2, numRows):
            for j in range(1, i):
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

        ans_arr = []
        for i in range(numRows):
            tmp_arr = []
            for j in range(i+1):
                tmp_arr.append(dp[i][j])
            ans_arr.append(tmp_arr)

        return ans_arr
