class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maintain a globalmin cost, maxprofit = price - globalmin cost
        if not prices:
            return 0
        minp = prices[0]
        res = 0
        for i in range(1, len(prices)):
            res = max(res, prices[i] - minp)
            minp = min(minp, prices[i])
        return res