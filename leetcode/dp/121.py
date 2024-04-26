class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_min = prices[0]
        dp = [-1]*len(prices)
        dp[0] = 0

        for i in range(1, len(prices)):
            buy_min = min(prices[i], buy_min)

            dp[i] = prices[i] - buy_min

        return max(dp)
