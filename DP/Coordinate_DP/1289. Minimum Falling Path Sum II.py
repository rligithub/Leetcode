class Solution1:  # top down dp - TLE
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        # minimum path sum 豪华升级版 --> 起始位置是 0 行任意一列，下一步不能在同一列（只要不要同一列就可以），走到m行 停止
        memo = {}
        n = len(grid[0])
        res = float('inf')
        for j in range(n):
            res = min(res, self.dfs(grid, 0, j, memo))
        return res

    def dfs(self, grid, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        m, n = len(grid), len(grid[0])

        # stop point
        if i == m - 1:
            return grid[i][j]

        # recursive
        res = float('inf')
        for pos in range(n):
            if pos != j:
                res = min(res, self.dfs(grid, i + 1, pos, memo) + grid[i][j])

        memo[(i, j)] = res

        return memo[(i, j)]


class Solution2:  # bottom up dp - TLE
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[float('inf')] * n for _ in range(m)]

        # initialization
        for j in range(n):
            dp[0][j] = grid[0][j]

        # transition formula
        for i in range(1, m):
            for j in range(n):
                dp[i][j] = float('inf')
                for k in range(n):
                    if k != j:
                        dp[i][j] = min(dp[i][j], dp[i - 1][k] + grid[i][j])

        # res = min(dp[-1])

        return min(dp[-1])


class Solution:  # bottom up dp - optimize --> 当前累积最小值 = 上一层累积最小值 + 当前值 --> maintain global min value
    def minFallingPathSum(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        dp = [[0] * n for _ in range(m)]

        # initialization
        for j in range(n):
            dp[0][j] = grid[0][j]

        # maintain global min value (===> paint house with k colors)
        for i in range(1, m):
            for j in range(n):
                min1 = float('inf')
                for k in range(n):
                    if k != j:
                        min1 = min(min1, dp[i - 1][k])
                dp[i][j] = min1 + grid[i][j]

        # res = min(dp[-1])
        return min(dp[-1])


