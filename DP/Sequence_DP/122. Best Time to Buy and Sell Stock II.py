class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 买卖股票，最多hold一股，当天可以买卖。求最大profit
        # status --> no stock + buy ; has stock + hold ; has stock + sell
        # 记录 天数 + 是否hold股票
        # 比较 action vs not_action

        memo = {}
        return self.dfs(prices, 0, False, memo)

    def dfs(self, prices, pos, has_stock, memo):
        if (pos, has_stock) in memo:
            return memo[(pos, has_stock)]

        # over range
        if pos > len(prices) - 1:
            return 0

        # action vs not_action
        not_action = self.dfs(prices, pos + 1, has_stock, memo)

        if has_stock:
            action = self.dfs(prices, pos + 1, False, memo) + prices[pos]
        else:
            action = self.dfs(prices, pos + 1, True, memo) - prices[pos]

        memo[(pos, has_stock)] = max(not_action, action)
        return memo[(pos, has_stock)]