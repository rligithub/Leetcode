class Solution1:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        # 按照结束时间排序
        rides.sort(key=lambda x: x[1])

        endTime = [rides[i][1] for i in range(len(rides))]

        # dp[i] 表示前i个行程带来的最大收益
        dp = [0 for _ in range(len(rides) + 1)]

        for i in range(1, len(rides) + 1):
            start, end, tip = rides[i - 1]

            # 找到结束时间小于等于当前行程开始时间的最后一个行程
            pos = bisect.bisect_right(endTime, start)
            # 两种可能，不算当前行程/算上当前行程
            dp[i] = max(dp[i - 1], end - start + tip + dp[pos])
        return dp[-1]