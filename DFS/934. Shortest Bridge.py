class Solution:  # DFS + DFS
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # similar to #827. Making A Large Island, but算的两岛的最短距离，而不是岛的面积

        m, n = len(grid), len(grid[0])
        # step1: distinguish two islands, markdown island1 and island2
        found_one = False
        self.res = float('inf')
        distance = [[float('inf')] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if not found_one:
                        self.dfs(grid, m, n, i, j, 2)
                        found_one = True
                    else:
                        # step2: for loop second island, search surroundings until meet find first island--> get min dist
                        self.dist(grid, m, n, i, j, 0, distance)

        return self.res - 1

    def dfs(self, grid, m, n, i, j, index):
        if i < 0 or i >= m or j < 0 or j >= n:
            return
        grid[i][j] = index

        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            x = i + dx
            y = j + dy
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                self.dfs(grid, m, n, x, y, index)

    def dist(self, grid, m, n, i, j, count, distance):

        distance[i][j] = min(distance[i][j], count)

        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            x = i + dx
            y = j + dy
            if 0 <= x < m and 0 <= y < n:
                if grid[x][y] == 2:  # 更新global值
                    self.res = min(self.res, count + 1)
                if count + 1 < distance[x][y]:  # 只有当更小距离的时候才操作
                    self.dist(grid, m, n, x, y, count + 1, distance)


class Solution2:  # DFS + DFS
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # similar to #827. Making A Large Island, but算的两岛的最短距离，而不是岛的面积

        m, n = len(grid), len(grid[0])
        # step1: distinguish two islands, markdown island1 and island2
        found_one = False
        self.res = float('inf')
        distance = [[float('inf')] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if not found_one:
                        self.dfs(grid, m, n, i, j, 2)
                        found_one = True
                        print(grid)
                    else:
                        # step2: for loop second island, search surroundings until meet find first island--> get min dist
                        self.dist(grid, m, n, i, j, 0, distance)

        return self.res - 1

    def dfs(self, grid, m, n, i, j, index):
        grid[i][j] = index

        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            x = i + dx
            y = j + dy
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                self.dfs(grid, m, n, x, y, index)

    def dist(self, grid, m, n, i, j, count, distance):
        if count >= distance[i][j]:
            return

        distance[i][j] = min(distance[i][j], count)

        if grid[i][j] == 2:
            self.res = min(self.res, count)
        else:
            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n:
                    self.dist(grid, m, n, x, y, count + 1, distance)




