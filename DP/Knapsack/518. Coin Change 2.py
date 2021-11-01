class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 求几种方式拿到target的钱数
        memo = {}
        return self.dfs(amount, coins, 0, memo)

    def dfs(self, amount, coins, pos, memo):
        if (amount, pos) in memo:
            return memo[(amount, pos)]

        if amount == 0:
            return 1
        if amount < 0:
            return 0
        if pos > len(coins) - 1:
            return 0

        pick = 0
        if amount >= coins[pos]:
            pick = self.dfs(amount - coins[pos], coins, pos, memo)
        not_pick = self.dfs(amount, coins, pos + 1, memo)

        memo[(amount, pos)] = pick + not_pick

        return memo[(amount, pos)]