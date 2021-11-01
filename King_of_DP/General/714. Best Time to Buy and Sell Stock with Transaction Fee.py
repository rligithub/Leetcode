class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # 买卖股票， 每次交易有transaction fees，求最大profits
        # buy/hold/sell

        memo = {}
        return self.dfs(prices, fee, 0, False, memo)

    def dfs(self, prices, fee, pos, has_stock, memo):
        if (pos, has_stock) in memo:
            return memo[(pos, has_stock)]

        if pos >= len(prices):
            return 0

        not_action = self.dfs(prices, fee, pos + 1, has_stock, memo)

        if has_stock:
            action = self.dfs(prices, fee, pos + 1, False, memo) + prices[pos] - fee
        else:
            action = self.dfs(prices, fee, pos + 1, True, memo) - prices[pos]

        memo[(pos, has_stock)] = max(not_action, action)
        return memo[(pos, has_stock)]