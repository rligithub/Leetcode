class Solution1:  # top down dp
    def maxProfit(self, prices: List[int]) -> int:
        # 买卖股票， 每次hold一股，最多买卖 2 次，求最大profit
        # status ==> buy1 ; hold1; sell1; buy2; hold2; sell2
        # not_action vs action

        memo = {}
        return self.dfs(prices, 0, False, 2, memo)

    def dfs(self, prices, pos, has_stock, k, memo):
        if (pos, has_stock, k) in memo:
            return memo[(pos, has_stock, k)]

        # stop point
        if pos > len(prices) - 1:
            return 0

        not_action = self.dfs(prices, pos + 1, has_stock, k, memo)

        action = 0
        if k > 0:
            if has_stock:  # if has_stock --> sell
                action = self.dfs(prices, pos + 1, False, k - 1, memo) + prices[pos]
            else:
                action = self.dfs(prices, pos + 1, True, k, memo) - prices[pos]

        memo[(pos, has_stock, k)] = max(not_action, action)
        return memo[(pos, has_stock, k)]


class Solution:  # status ==> buy1 ; sell1; buy2; sell2
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        buy1, buy2 = float('-inf'), float('-inf')
        sold1, sold2 = 0, 0

        for p in prices:
            buy1 = max(buy1, -p)
            sold1 = max(sold1, buy1 + p)
            buy2 = max(buy2, sold1 - p)
            sold2 = max(sold2, buy2 + p)
        return max(sold1, sold2)
