class Solution1:
    def minDays(self, grid: List[List[int]]) -> int:
        # step1: for loop all nodes to check if there is only one island? if no --> return 0
        m, n = len(grid), len(grid[0])

        count = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    self.dfs(grid, m, n, i, j, visited)
                    count += 1
                    if count >= 2:
                        return 0
        if count == 0:
            return 0

        # step2: for each land in island, assume it's removed --> check if there are zero or two more islands, if yes --> return 1

        for (x, y) in visited:
            removed_land = (x, y)
            grid[x][y] = 0
            new_count = 0
            new_visited = set()
            for (i, j) in visited:
                if grid[i][j] == 1 and (i, j) not in new_visited:
                    self.dfs(grid, m, n, i, j, new_visited)
                    new_count += 1
                    if new_count >= 2:
                        return 1
            if new_count != 1:
                return 1
            grid[x][y] = 1

        # step3: otherwise, return 2 at most
        return 2

    def dfs(self, grid, m, n, i, j, visited):
        visited.add((i, j))

        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            x = i + dx
            y = j + dy
            if 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid[x][y] == 1:
                self.dfs(grid, m, n, x, y, visited)


