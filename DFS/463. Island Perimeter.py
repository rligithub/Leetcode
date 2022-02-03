class Solution1:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # 出界 或者 遇到 water ---> 边边 + 1
        m, n = len(grid), len(grid[0])

        count = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += self.dfs(grid, i, j, visited)
                    return count

    def dfs(self, grid, i, j, visited):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return 1

        if (i, j) in visited:
            return 0

        visited.add((i, j))
        total = 0
        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            x = i + dx
            y = j + dy
            total += self.dfs(grid, x, y, visited)
        return total


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # 出界 或者 遇到 water ---> 边边 + 1
        m, n = len(grid), len(grid[0])

        self.total = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j, visited)
                    return self.total

    def dfs(self, grid, i, j, visited):

        visited.add((i, j))
        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            x = i + dx
            y = j + dy
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                if (x, y) not in visited:
                    self.dfs(grid, x, y, visited)
            else:
                self.total += 1

