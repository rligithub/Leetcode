class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        queue = collections.deque()
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "*":
                    queue.append((i, j, 0))
                    visited.add((i, j))
                    break
        while queue:
            i, j, dist = queue.popleft()
            if grid[i][j] == '#':
                return dist

            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid[x][y] != "X":
                    queue.append((x, y, dist + 1))
                    visited.add((x, y))
        return -1 