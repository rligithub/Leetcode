class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # put all lands that can be walkable from boundary into visited
        visited = set()
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    if grid[i][j] == 1 and (i, j) not in visited:
                        self.dfs(grid, m, n, i, j, visited)

        # if land not in visited? count ++
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    count += 1
        return count

    def dfs(self, grid, m, n, i, j, visited):
        visited.add((i, j))
        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            x = i + dx
            y = j + dy
            if 0 <= x < m and 0 <= y < n and grid[i][j] == 1 and (x, y) not in visited:
                self.dfs(grid, m, n, x, y, visited)