class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        # 一排球 找球最后落下的位置 --> 如果中间卡住，返回-1，否则返回落下的位置
        m, n = len(grid), len(grid[0])

        res = [0] * n
        for j in range(n):
            col = self.dfs(grid, m, n, 0, j)
            res[j] = col
        return res

    def dfs(self, grid, m, n, i, j):
        if i == m:
            return j
        # find 相邻的 格子
        y = j + grid[i][j]
        if 0 <= y < n and grid[i][y] == grid[i][j]:  # 相邻的格子不能形成V型（即不能为不同值）且不能和墙相邻
            return self.dfs(grid, m, n, i + 1, y)
        else:
            return -1


