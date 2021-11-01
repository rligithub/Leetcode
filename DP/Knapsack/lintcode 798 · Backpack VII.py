
class Solution1:  # bottom up dp
    """
    @param n: the money of you
    @param prices: the price of rice[i]
    @param weight: the weight of rice[i]
    @param amounts: the amount of rice[i]
    @return: the maximum weight
    """

    def backPackVII(self, n, prices, weight, amounts):
        m = len(prices)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # i --> items
        # j --> money
        # k --> # of items
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # not_pick
                dp[i][j] = dp[i - 1][j]
                for k in range(amounts[i - 1] + 1):
                    # dp[i][j] = max(not_pick, pick)
                    # items - limited quantity (no infinite)
                    if j - k * prices[i - 1] >= 0:
                        dp[i][j] = max(dp[i][j], dp[i - 1][j - k * prices[i - 1]] + k * weight[i - 1])

        return dp[-1][-1]



n = 8
prices = [3,2]
weight = [300,160]
amounts = [1,6]

a= Solution()
print(a.backPackVII(n, prices, weight, amounts))