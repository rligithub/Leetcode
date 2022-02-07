class Solution1:  # for loop twice
    def closedIsland(self, grid: List[List[int]]) -> int:
        # 找有几块 四周被水包围的islands
        # num of island - num of island that connected with 边边

        m, n = len(grid), len(grid[0])

        # step1: find num of islands that connected with 边边 --> saved it in a set
        visited = set()
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    if grid[i][j] == 0 and (i, j) not in visited:
                        self.dfs(grid, m, n, i, j, visited)

        # step2: find rest of islands
        count = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0 and (i, j) not in visited:
                    count += 1
                    self.dfs(grid, m, n, i, j, visited)

        return count

    def dfs(self, grid, m, n, i, j, visited):
        visited.add((i, j))

        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            x = i + dx
            y = j + dy
            if 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid[x][y] == 0:
                self.dfs(grid, m, n, x, y, visited)


class Solution2:  # for loop once
    def closedIsland(self, grid: List[List[int]]) -> int:
        # num of island - num of island that connected with 边边

        m, n = len(grid), len(grid[0])

        visited = set()

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and (i, j) not in visited:
                    if self.dfs(grid, m, n, i, j, visited):
                        count += 1
        return count

    def dfs(self, grid, m, n, i, j, visited):
        if i == 0 or j == 0 or i == m - 1 or j == n - 1:
            return False

        visited.add((i, j))
        res = True
        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            x = i + dx
            y = j + dy
            if 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid[x][y] == 0:
                res &= self.dfs(grid, m, n, x, y, visited)  # can't not do early return --> need to add all connected islands into visited, so we won't visit again

        return res


class Solution:  # for loop once
    def closedIsland(self, grid: List[List[int]]) -> int:
        # num of island - num of island that connected with 边边

        m, n = len(grid), len(grid[0])

        visited = set()

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and (i, j) not in visited:
                    if self.dfs(grid, m, n, i, j, visited) == 0:
                        count += 1
        return count

    def dfs(self, grid, m, n, i, j, visited):
        if i == 0 or j == 0 or i == m - 1 or j == n - 1:
            return 1

        visited.add((i, j))
        res = 0
        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            x = i + dx
            y = j + dy
            if 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid[x][y] == 0:
                res += self.dfs(grid, m, n, x, y, visited)  # can't not do early return --> need to add all connected islands into visited, so we won't visit again

        return res