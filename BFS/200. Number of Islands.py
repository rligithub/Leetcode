class Solution:  # BFS
    def numIslands(self, grid: List[List[str]]) -> int:
        # 几个islands --> DFS --> marked down connected island
        m, n = len(grid), len(grid[0])

        visited = set()
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visited:
                    count += 1
                    self.bfs(grid, i, j, m, n, visited)
        return count

    def bfs(self, grid, i, j, m, n, visited):
        queue = collections.deque()
        queue.append((i, j))
        visited.add((i, j))

        while queue:
            ii, jj = queue.popleft()

            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                x = ii + dx
                y = jj + dy
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid[x][y] == '1':
                    queue.append((x, y))
                    visited.add((x, y))