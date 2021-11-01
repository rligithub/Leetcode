class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 求有几种方式组成 amount， 每种coins可以用无限次
        memo = {}
        res = self.dfs(coins, amount, 0, memo)

        return res

    def dfs(self, coins, amount, pos, memo):
        if (amount, pos) in memo:
            return memo[(amount, pos)]

        if amount == 0:
            return 1

        if amount < 0 or pos == len(coins):
            return 0

        pick = 0
        if amount >= coins[pos]:
            # 一个coin可以用无限次
            pick = self.dfs(coins, amount - coins[pos], pos, memo)
        not_pick = self.dfs(coins, amount, pos + 1, memo)

        memo[(amount, pos)] = pick + not_pick
        return memo[(amount, pos)]