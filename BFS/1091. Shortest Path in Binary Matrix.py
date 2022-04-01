class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        m, n = len(grid), len(grid[0])

        queue = collections.deque()
        queue.append((0, 0, 1))
        visited = set()
        visited.add((0, 0))

        while queue:

            i, j, step = queue.popleft()
            if i == m - 1 and j == n - 1:
                return step

            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1):
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid[x][y] == 0:
                    queue.append((x, y, step + 1))
                    visited.add((x, y))

        return -1