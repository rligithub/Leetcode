class Solution: # BFS
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # 找出有几块 不同的 island --> 用路径来标记 island形状的不同 ---> BFS 不能一层一层看路径，需要 每次看4个方向然后结尾 ---> start + dire + end

        m, n = len(grid), len(grid[0])
        res = set()
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    path = self.bfs(grid, m, n, i, j, visited)
                    res.add(path)
        return len(res)

    def bfs(self, grid, m, n, i, j, visited):
        queue = collections.deque()
        queue.append((i, j))
        visited.add((i, j))
        path = 's'
        while queue:
            i, j = queue.popleft()
            for dx, dy, dire in (1, 0, 'd'), (0, 1, 'r'), (0, -1, 'l'), (-1, 0, 'u'):
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid[x][y] == 1:
                    queue.append((x, y))
                    visited.add((x, y))
                    path += dire
            path += 'e'

        return path


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # 找出有几块 不同的 island --> 用路径来标记 island形状的不同 ---> BFS path为 连接的所有点 减去 最初的起始点坐标

        m, n = len(grid), len(grid[0])
        res = set()
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    path = self.bfs(grid, m, n, i, j, visited)
                    res.add(path)
        return len(res)

    def bfs(self, grid, m, n, start_i, start_j, visited):
        queue = collections.deque()
        queue.append((start_i, start_j))
        visited.add((start_i, start_j))
        path = 's'
        while queue:
            i, j = queue.popleft()
            for dx, dy in (1, 0), (0, 1), (0, -1), (-1, 0):
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid[x][y] == 1:
                    queue.append((x, y))
                    visited.add((x, y))
                    path += str(x - start_i) + str(y - start_j)

        return path
