class Solution1:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 找出 island的最大面积
        m, n = len(grid), len(grid[0])
        res = 0

        visited = set()
        for i in range(m):
            for j in range(n):
                self.count = 1
                if grid[i][j] == 1 and (i, j) not in visited:
                    self.dfs(grid, m, n, i, j, visited)
                    res = max(res, self.count)

        return res

    def dfs(self, grid, m, n, i, j, visited):
        visited.add((i, j))

        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            x = i + dx
            y = j + dy
            if 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid[x][y] == 1:
                self.count += 1
                self.dfs(grid, m, n, x, y, visited)


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 找出 island的最大面积
        m, n = len(grid), len(grid[0])
        res = 0

        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    res = max(res, self.dfs(grid, m, n, i, j, visited))

        return res

    def dfs(self, grid, m, n, i, j, visited):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
            return 0

        if (i, j) in visited:
            return 0
        visited.add((i, j))
        count = 1
        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            x = i + dx
            y = j + dy

            count += self.dfs(grid, m, n, x, y, visited)
        return count
