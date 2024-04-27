class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[1]*5 for _ in range(n)]

        for i in range(1, n):
            for j in range(1, 5):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]

        return sum(dp[n-1])
