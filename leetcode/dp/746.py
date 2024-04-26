class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0]*(n+2)
        dp[1] = cost[0]
        dp[2] = cost[1]

        for i in range(3, n+2):
            dp[i] = min(dp[i-1], dp[i-2])
            if i - 1 < n:
                dp[i] += cost[i-1]

        return dp[n+1]
