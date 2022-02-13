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


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 几个islands --> DFS --> marked down connected island
        m, n = len(grid), len(grid[0])

        visited = set()
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visited:
                    count += 1
                    self.dfs(grid, i, j, m, n, visited)
        return count

    def dfs(self, grid, i, j, m, n, visited):

        visited.add((i, j))
        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            x = i + dx
            y = j + dy
            if 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid[x][y] == '1':
                self.dfs(grid, x, y, m, n, visited)
