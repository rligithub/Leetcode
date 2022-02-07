class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        # 给一个起始位置和要涂成的颜色 --> 把相邻的同一个色块的边界或者如果该色块连着别的颜色 涂成该颜色 --> 返回 grid
        # 注意 只涂 boundary
        m, n = len(grid), len(grid[0])

        visited = set()
        self.dfs(grid, m, n, row, col, color, grid[row][col], visited)

        return grid

    def dfs(self, grid, m, n, i, j, color, org_color, visited):

        # case1：边界点
        if i == 0 or i == m - 1 or j == 0 or j == n - 1:
            grid[i][j] = color
        visited.add((i, j))
        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            x = i + dx
            y = j + dy
            if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                if grid[x][y] == org_color:
                    self.dfs(grid, m, n, x, y, color, org_color, visited)
                else:
                    grid[i][j] = color  # case2：如果四周连接别的颜色--> 则把该颜色涂成新颜色


