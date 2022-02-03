class Solution1:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # 找出有几块 不同的 island --> 用路径来标记 island形状的不同
        m, n = len(grid), len(grid[0])

        visited = set()
        res = set()
        for i in range(m):
            for j in range(n):
                path = []
                if grid[i][j] == 1 and (i, j) not in visited:
                    self.dfs(grid, m, n, i, j, visited, path)
                    print(1, path)
                    res.add(tuple(path))
        return len(res)

    def dfs(self, grid, m, n, i, j, visited, path):
        if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited or grid[i][j] == 0:
            return
        visited.add((i, j))

        for dx, dy, dire in (1, 0, 'd'), (0, 1, 'r'), (-1, 0, 'u'), (0, -1, 'l'):
            x = i + dx
            y = j + dy
            path.append(dire)
            self.dfs(grid, m, n, x, y, visited, path)


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # 找出有几块 不同的 island --> 用路径来标记 island形状的不同
        m, n = len(grid), len(grid[0])

        visited = set()
        res = set()
        for i in range(m):
            for j in range(n):
                path = []
                if grid[i][j] == 1 and (i, j) not in visited:
                    self.dfs(grid, m, n, i, j, visited, path)
                    print(1, path)
                    res.add(tuple(path))
        return len(res)

    def dfs(self, grid, m, n, i, j, visited, path):
        visited.add((i, j))
        for dx, dy, dire in (1, 0, 'd'), (0, 1, 'r'), (-1, 0, 'u'), (0, -1, 'l'):
            x = i + dx
            y = j + dy
            if 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid[x][y] == 1:
                path.append(dire)
                self.dfs(grid, m, n, x, y, visited, path)
                path.append('')

