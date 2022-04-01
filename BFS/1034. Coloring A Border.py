class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        # 给一个起始位置和要涂成的颜色 --> 把相邻的同一个色块的边界或者如果该色块连着别的颜色 涂成该颜色 --> 返回 grid
        # 注意 只涂 boundary

        old_color = grid[row][col]

        m, n = len(grid), len(grid[0])

        queue = collections.deque()
        queue.append((row, col))
        visited = set()
        visited.add((row, col))

        while queue:
            i, j = queue.popleft()
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                grid[i][j] = color

            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                    if grid[x][y] == old_color:
                        queue.append((x, y))
                        visited.add((x, y))
                    else:
                        grid[i][j] = color
        return grid
