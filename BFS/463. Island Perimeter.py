class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
        while queue:
            i, j = queue.popleft()

            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                x = i + dx
                y = j + dy
                if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != 1:
                    count += 1
        return count
