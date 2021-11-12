class Solution1:  # TLE
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        memo = {}
        return self.dfs(n, minProfit, group, profit, 0, 0, memo)

    def dfs(self, n, minProfit, group, profit, pos, p, memo):
        # pos, cur_profit,people
        if (pos, p, n) in memo:
            return memo[(pos, p, n)]

        if pos == len(group):
            return p >= minProfit

        mod = 10 ** 9 + 7

        pick = 0
        if n >= group[pos]:
            pick = self.dfs(n - group[pos], minProfit, group, profit, pos + 1, p + profit[pos], memo)
        not_pick = self.dfs(n, minProfit, group, profit, pos + 1, p, memo)

        memo[(pos, p, n)] = (pick + not_pick) % mod
        return memo[(pos, p, n)]


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        memo = {}
        return self.dfs(n, minProfit, group, profit, 0, 0, memo)

    def dfs(self, n, minProfit, group, profit, pos, p, memo):
        # pos, cur_profit,people
        if (pos, p, n) in memo:
            return memo[(pos, p, n)]

        if pos == len(group):
            return p >= minProfit

        mod = 10 ** 9 + 7

        pick = 0
        if n >= group[pos]:
            pick = self.dfs(n - group[pos], minProfit, group, profit, pos + 1, min(minProfit, p + profit[pos]), memo)
        not_pick = self.dfs(n, minProfit, group, profit, pos + 1, p, memo)

        memo[(pos, p, n)] = (pick + not_pick) % mod
        return memo[(pos, p, n)]