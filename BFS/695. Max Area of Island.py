class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    res = max(res, self.bfs(grid, m, n, i, j, visited))
        return res

    def bfs(self, grid, m, n, i, j, visited):

        queue = collections.deque()
        queue.append((i, j))
        visited.add((i, j))
        count = 0

        while queue:
            i, j = queue.popleft()
            count += 1

            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid[x][y] == 1:
                    queue.append((x, y))
                    visited.add((x, y))
        return count


