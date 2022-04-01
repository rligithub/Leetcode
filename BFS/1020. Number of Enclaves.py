class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # return number of land cells that is not walkable from the boundary
        m, n = len(grid), len(grid[0])
        queue = collections.deque()
        visited = set()

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
                    if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                        queue.append((i, j))
                        visited.add((i, j))

        while queue:
            i, j = queue.popleft()

            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid[x][y] == 1:
                    queue.append((x, y))
                    visited.add((x, y))

        return count - len(visited)
