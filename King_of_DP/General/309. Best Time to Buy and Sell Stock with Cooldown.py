class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 买卖股票，次数不受限，但是每个交易结束需要cool down一天
        # buy/hold/sell/cooldown
        memo = {}
        return self.dfs(prices, 0, False, False, memo)

    def dfs(self, prices, pos, has_stock, need_cooldown, memo):
        if (pos, has_stock, need_cooldown) in memo:
            return memo[(pos, has_stock, need_cooldown)]

        # base case --> last day
        if pos == len(prices):
            return 0

        # not action(hold/cooldown) vs action(buy/sell)

        # if not_action --> need_cooldown == False
        not_action = self.dfs(prices, pos + 1, has_stock, False, memo)

        # action --> if not need cooldown
        # check if has stock --> buy / sell
        action = 0
        if need_cooldown == False:
            if has_stock:
                action = self.dfs(prices, pos + 1, False, True, memo) + prices[pos]
            else:
                action = self.dfs(prices, pos + 1, True, False, memo) - prices[pos]

        memo[(pos, has_stock, need_cooldown)] = max(not_action, action)
        return memo[(pos, has_stock, need_cooldown)]