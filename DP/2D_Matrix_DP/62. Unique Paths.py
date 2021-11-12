class Solution:  # top down dp
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        return self.dfs(m, n, 0, 0, memo)

    def dfs(self, m, n, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        # 终点检查 -- last position
        if i == m - 1 and j == n - 1:
            return 1
        # 出界检查
        if i > m - 1 or j > n - 1:
            return 0

        memo[(i, j)] = self.dfs(m, n, i + 1, j, memo) + self.dfs(m, n, i, j + 1, memo)

        return memo[(i, j)]