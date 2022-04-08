class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        distance = [[-1] * n for _ in range(m)]

        # step1: start from each land, update the water's distance --> update min distance on each water
        queue = collections.deque()
        visited = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))
                    visited.add((i, j))

        if len(queue) == 0 or len(queue) == m * n:
            return -1

        while queue:
            i, j, dist = queue.popleft()
            if distance[i][j] == -1 or dist < distance[i][j]:
                distance[i][j] = dist

            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid[x][y] == 0:
                    queue.append((x, y, dist + 1))
                    visited.add((x, y))

        # step2: for loop all water's distance --> return max distance
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, distance[i][j])
        return res