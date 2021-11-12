class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        memo = {}
        res = self.dfs(coins, amount, memo)
        if res == float('inf'):
            return -1
        else:
            return res

    def dfs(self, coins, amount, memo):
        if amount in memo:
            return memo[amount]

        if amount == 0:
            return 0

        if amount < 0:
            return float('inf')

        res = float('inf')
        for coin in coins:
            res = min(res, self.dfs(coins, amount - coin, memo) + 1)

        memo[amount] = res
        return memo[amount]

class Solution1: # bottom up dp
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0 or not coins:
            return 0
        coins.sort()
        # dp[i] = min # of coins used to get amount of i
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin and dp[i - coin] != float('inf'):
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[-1] != float('inf'):
            return dp[-1]
        else:
            return -1