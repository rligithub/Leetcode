class Solution1:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        visited = set()
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:
                    if self.dfs(grid, m, n, grid[i][j], i, j, None, visited):  # if cycle
                        return True
        return False

    def dfs(self, grid, m, n, val, i, j, prev, visited):
        if (i, j) in visited:
            return True

        visited.add((i, j))

        for dx, dy in (1, 0), (0, 1), (0, -1), (-1, 0):
            x = i + dx
            y = j + dy
            if 0 <= x < m and 0 <= y < n and (x, y) != prev and grid[x][y] == val:
                if self.dfs(grid, m, n, val, x, y, (i, j), visited):
                    return True

        return False


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        visited = set()
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:
                    if self.dfs(grid, m, n, grid[i][j], i, j, None, visited):  # if cycle
                        return True

        return False

    def dfs(self, grid, m, n, val, i, j, prev, visited):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != val:
            return False

        if (i, j) in visited:
            return True

        visited.add((i, j))

        for dx, dy in (1, 0), (0, 1), (0, -1), (-1, 0):
            x = i + dx
            y = j + dy
            if (x, y) != prev:  # 需要确保 不往回走 --> 比较parent和grandson 因为前一个 相同val已经存在visited里了
                if self.dfs(grid, m, n, val, x, y, (i, j), visited):
                    return True

        return False