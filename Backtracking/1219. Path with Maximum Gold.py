class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # 注意：不能走出网格边界，也不能进入值为0的无黄金网格
        res = 0
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    res = max(res, self.dfs(grid, m, n, i, j, set()))

        return res

    def dfs(self, grid, m, n, i, j, visited):

        res = grid[i][j]
        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            x = i + dx
            y = j + dy
            if 0 <= x < m and 0 <= y < n and grid[x][y] != 0 and (x, y) not in visited:
                visited.add((i, j))
                res = max(res, self.dfs(grid, m, n, x, y, visited) + grid[i][j])
                visited.remove((i, j))

        return res


