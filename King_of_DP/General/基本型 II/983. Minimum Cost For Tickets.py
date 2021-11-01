class Solution1:  # super fast
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # 给三种火车pass： 1day，7day，30day 求如果使得days里date都坐火车，求最便宜要花多少钱
        memo = {}
        return self.dfs(days, costs, 0, memo)

    def dfs(self, days, costs, pos, memo):
        if pos in memo:
            return memo[pos]

        if pos == len(days):
            return 0

            # 找出比当前covered days 要大的第一位index
        pos1 = bisect.bisect_left(days, days[pos] + 1)
        pick1 = self.dfs(days, costs, pos1, memo) + costs[0]

        pos7 = bisect.bisect_left(days, days[pos] + 7)
        pick7 = self.dfs(days, costs, pos7, memo) + costs[1]

        pos30 = bisect.bisect_left(days, days[pos] + 30)
        pick30 = self.dfs(days, costs, pos30, memo) + costs[2]

        memo[pos] = min(pick1, pick7, pick30)
        return memo[pos]


class Solution:  # slower
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        return self.dfs(days, costs, 0, memo)

    def dfs(self, days, costs, pos, memo):
        if pos in memo:
            return memo[pos]

        if pos == len(days):
            return 0

        res = float('inf')
        nxt_pos = pos
        for cost, d in zip(costs, [1, 7, 30]):
            # 找出 un-covered days
            while nxt_pos < len(days) and days[nxt_pos] < days[pos] + d:
                nxt_pos += 1
            res = min(res, cost + self.dfs(days, costs, nxt_pos, memo))

        memo[pos] = res
        return memo[pos]






