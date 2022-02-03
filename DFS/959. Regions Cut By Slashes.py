class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        # 将网格分成若干区域，并求区域的个数 --> similar to number of islands
        # 注意 2x2 不行， 反例 '//' '//'
        m, n = len(grid), len(grid[0])

        # build graph 3x3 for each '/' or '\\'
        graph = [[0] * 3 * n for _ in range(3 * m)]

        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '/':
                    graph[3 * i][3 * j + 2] = 1
                    graph[3 * i + 1][3 * j + 1] = 1
                    graph[3 * i + 2][3 * j] = 1
                elif grid[i][j] == '\\':
                    graph[3 * i][3 * j] = 1
                    graph[3 * i + 1][3 * j + 1] = 1
                    graph[3 * i + 2][3 * j + 2] = 1

        # count num of island --> island ==> '0'
        for i in range(3 * m):
            for j in range(3 * n):
                if graph[i][j] == 0:
                    res += 1
                    self.dfs(graph, 3 * m, 3 * n, i, j)
        return res

    def dfs(self, graph, m, n, i, j):
        graph[i][j] = 1

        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            x = i + dx
            y = j + dy
            if 0 <= x < m and 0 <= y < n and graph[x][y] == 0:
                self.dfs(graph, m, n, x, y)
