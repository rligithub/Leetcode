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


class Solution:  # complicated
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # use 711. Number of Distinct Islands II method!!!!!
        # step1：DFS找出 island， 把每一个坐标存起来
        # step2: sort一下这些点，以第一个点为原点，replace原来每个点为 每个点对于原点的相对坐标
        # step3：把normalized后的island形状 坐标 存到 hashset里
        # step4：求hashset的大小

        m, n = len(grid), len(grid[0])

        res = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:  # find an islands, put all coordinates of lands
                    island = []
                    self.dfs(grid, m, n, i, j, island)
                    res.add(self.normalize(island))
        return len(res)

    def dfs(self, grid, m, n, i, j, path):

        grid[i][j] = 0
        path.append((i, j))
        for dx, dy in (1, 0), (0, 1), (0, -1), (-1, 0):
            x = i + dx
            y = j + dy
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                self.dfs(grid, m, n, x, y, path)

    def normalize(self, island):  # normalize an island

        # convert to new coordinates---> replace ---> relative position justification based on shape[0]
        island.sort()
        for i in range(len(island) - 1, -1, -1):
            island[i] = (island[i][0] - island[0][0], island[i][1] - island[0][1])

        return tuple(island)