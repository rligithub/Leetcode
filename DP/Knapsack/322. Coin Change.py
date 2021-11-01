class Solution:  # top down dp
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