class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # 从一堆数组中选一几个数字，数字的cost 为target，求最大能组成的数字。无限选
        memo = {}
        res = self.dfs(cost, target, 0, memo)

        if res > 0:
            return str(res)
        else:
            return '0'

    def dfs(self, cost, target, pos, memo):
        if (target, pos) in memo:
            return memo[(target, pos)]

        if pos == len(cost) or target < 0:
            return float('-inf')

        if target == 0:
            return 0

        not_pick = self.dfs(cost, target, pos + 1, memo)

        pick = self.dfs(cost, (target - cost[pos]), pos, memo) * 10 + pos + 1

        memo[(target, pos)] = max(not_pick, pick)
        return memo[(target, pos)]