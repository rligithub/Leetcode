class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        # 找有几块不同的island --> 形状旋转后不同 --> 8个方向旋转

        # step1：DFS找出 island， 把每一个坐标存起来
        # step2: 对于这个island上的每个点旋转8个方向，存在size为8的数组里【list of list】，sort一下这些点，以第一个点为原点，replace原来每个点为 每个点对于原点的相对坐标，再把整个size为8的数组 sort一下，return第一个island的图形
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

    def normalize(self,
                  island):  # normalize an island, 8 possible changes, 0, 90, 180, 270 and mirror's 0, 90, 180, 270
        shapes = [[] for _ in range(8)]
        for i, j in island:
            idx = 0
            for x, y in [(i, j), (j, i)]:  # mirror below
                for dx, dy in (1, 1), (1, -1), (-1, 1), (-1, -1):  # four directions
                    newX, newY = x * dx, y * dy
                    shapes[idx].append((newX, newY))
                    idx += 1

        # convert to new coordinates---> replace ---> relative position justification based on shape[0]
        for shape in shapes:
            shape.sort()
            for i in range(len(shape) - 1, -1, -1):
                shape[i] = (shape[i][0] - shape[0][0], shape[i][1] - shape[0][1])

        shapes.sort()
        return tuple(shapes[0])