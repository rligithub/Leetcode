class Solution1:  # Top down DP --> TLE
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        # 第一行任意一点出发，向下走，相邻两行不能在同一列，走到最后一行停止，求min sum
        # 类似刷房子那道题，相邻两个房子不能刷同一个颜色。优化-->每次选每行中最便宜的和第二便宜的
        memo = {}
        res = float('inf')
        for j in range(len(grid[0])):
            res = min(res, self.dfs(grid, 0, j, memo))
        return res

    def dfs(self, grid, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        # 看下面的循环--> j肯定在0...len(grid[0])中选，不用做出界判断

        if i == len(grid) - 1:
            return grid[i][j]

        res = float('inf')
        for col in range(len(grid[0])):
            if col != j:
                # 注意res 是累积比较的值
                res = min(res, self.dfs(grid, i + 1, col, memo) + grid[i][j])

        memo[(i, j)] = res
        return memo[(i, j)]


class Solution:  # Bottom up dp - optimize
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[0] * n for _ in range(m)]

        for j in range(n):
            dp[0][j] = grid[0][j]

        for i in range(1, m):
            for j in range(n):
                min1 = float('inf')
                for k in range(n):
                    if k != j:
                        min1 = min(min1, dp[i - 1][k])
                # 上一层累积最小 + 当前值
                dp[i][j] = min1 + grid[i][j]

        return min(dp[-1])













