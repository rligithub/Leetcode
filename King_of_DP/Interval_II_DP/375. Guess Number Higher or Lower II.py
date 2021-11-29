class Solution:
    def getMoneyAmount(self, n: int) -> int:
        memo = {}

        return self.dfs(1, n, memo)

    def dfs(self, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i >= j:
            return 0

        # guess num k
        res = float('inf')
        for k in range(i, j + 1):
            higher = self.dfs(i, k - 1, memo)
            lower = self.dfs(k + 1, j, memo)
            res = min(res, max(lower, higher) + k)

        memo[(i, j)] = res
        return res