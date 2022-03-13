class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = [i, j]
                elif grid[i][j] == 0:
                    count += 1
        self.res = 0
        self.dfs(grid, m, n, start[0], start[1], count, set())
        return self.res

    def dfs(self, grid, m, n, i, j, count, visited):
        if (i, j) in visited:
            return

        if grid[i][j] == 2 and len(visited) == count + 1:
            self.res += 1
            return

        visited.add((i, j))
        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            x = i + dx
            y = j + dy
            if 0 <= x < m and 0 <= y < n and grid[x][y] != -1:
                self.dfs(grid, m, n, x, y, count, visited)
        visited.remove((i, j))