class Solution:
    def divisorGame(self, n: int) -> bool:
        if n == 1:
            return False
        dp = [False]*(n+1)
        dp[2] = True
        for i in range(3, n+1):
            # ищем делители
            for j in range(1, i):
                # хорошая позиция для Алисы та,
                # из которогой она может кинуть врага в плохую
                if i % j == 0:
                    if dp[i-j] == False:
                        dp[i] = True
                        continue

        return dp[n]
