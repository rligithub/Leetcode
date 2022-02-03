class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 几个islands --> DFS --> marked down connected island
        m, n = len(grid), len(grid[0])

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j, m, n)
        return count

    def dfs(self, grid, i, j, m, n):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
            return

        grid[i][j] = 'X'
        for x, y in (1, 0), (0, 1), (-1, 0), (0, -1):
            self.dfs(grid, i + x, j + y, m, n)