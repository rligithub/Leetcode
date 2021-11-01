class Solution1:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # 移球，上下左右移动，最多移动 maxMove次，求移出界的次数有多少次

        memo = {}
        return self.dfs(m, n, maxMove, startRow, startColumn, memo)

    def dfs(self, m, n, k, i, j, memo):
        if (k, i, j) in memo:
            return memo[(k, i, j)]

        if k < 0:
            return 0

        if i < 0 or i >= m or j < 0 or j >= n:
            return 1
        mod = 10 ** 9 + 7
        res = 0
        for dx, dy in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            res += self.dfs(m, n, k - 1, i + dx, j + dy, memo)

        memo[(k, i, j)] = res % mod
        return memo[(k, i, j)]


class Solution:  # faster
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # 移球，上下左右移动，最多移动 maxMove次，求移出界的次数有多少次

        memo = {}
        return self.dfs(m, n, maxMove, startRow, startColumn, memo)

    def dfs(self, m, n, k, i, j, memo):
        if (k, i, j) in memo:
            return memo[(k, i, j)]

        if k < 0:
            return 0

        if i < 0 or i >= m or j < 0 or j >= n:
            return 1

        mod = 10 ** 9 + 7

        up = self.dfs(m, n, k - 1, i + 1, j, memo)
        down = self.dfs(m, n, k - 1, i - 1, j, memo)
        left = self.dfs(m, n, k - 1, i, j - 1, memo)
        right = self.dfs(m, n, k - 1, i, j + 1, memo)

        memo[(k, i, j)] = (up + down + left + right) % mod
        return memo[(k, i, j)]