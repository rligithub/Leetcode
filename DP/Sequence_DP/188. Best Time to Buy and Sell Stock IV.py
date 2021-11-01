class Solution:  # top down dp
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # 买卖股票，可以完成k次交易，每次hold一个股票，求最大profit
        # status --> buy / hold / sell

        memo = {}
        return self.dfs(prices, k, 0, False, memo)

    def dfs(self, prices, k, pos, has_stock, memo):
        if (k, pos, has_stock) in memo:
            return memo[(k, pos, has_stock)]

        # stop point
        if pos > len(prices) - 1:
            return 0

            # not_action vs action(buy/sell)
        not_action = self.dfs(prices, k, pos + 1, has_stock, memo)

        action = 0
        if k > 0:
            if has_stock:
                action = self.dfs(prices, k - 1, pos + 1, False, memo) + prices[pos]
            else:
                action = self.dfs(prices, k, pos + 1, True, memo) - prices[pos]

        memo[(k, pos, has_stock)] = max(not_action, action)
        return memo[(k, pos, has_stock)]