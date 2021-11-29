class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        # connect all left nodes to the right
        # connect remaining right nodes to the left (preprocessing min cost of connecting right node to left node)

        m, n = len(cost), len(cost[0])

        minCost = [float('inf')] * n
        for j in range(n):
            for i in range(m):
                minCost[j] = min(minCost[j], cost[i][j])

        memo = {}
        return self.dfs(cost, minCost, 0, 0, memo)

    def dfs(self, cost, minCost, pos, state, memo):
        if (pos, state) in memo:
            return memo[(pos, state)]

        if pos == len(cost):
            res = 0
            for j in range(len(cost[0])):
                if not state & (1 << j):
                    res += minCost[j]
            memo[(pos, state)] = res
            return memo[(pos, state)]

        res = float('inf')
        for j in range(len(cost[0])):
            res = min(res, self.dfs(cost, minCost, pos + 1, state | (1 << j), memo) + cost[pos][j])

        memo[(pos, state)] = res
        return memo[(pos, state)]
