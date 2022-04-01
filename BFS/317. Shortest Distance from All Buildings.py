class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # similar to 286 walls and gates
        # satrt from building --> better than start from empty land
        m, n = len(grid), len(grid[0])
        distances = [[0] * n for _ in range(m)]
        reach = [[0] * n for _ in range(m)]

        # step1: bfs --> updates distances and reach
        building_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    building_count += 1
                    self.bfs(grid, m, n, i, j, distances, reach)

        # step2: find min distances with reach[i][j] == building
        res = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and distances[i][j] > 0 and reach[i][j] == building_count:
                    res = min(res, distances[i][j])
        if res < float('inf'):
            return res
        return -1

    def bfs(self, grid, m, n, i, j, distances, reach):
        queue = collections.deque()
        queue.append((0, i, j))
        visited = set()
        visited.add((i, j))

        while queue:
            dist, i, j = queue.popleft()
            distances[i][j] += dist
            reach[i][j] += 1

            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 0 and (x, y) not in visited:
                    queue.append((dist + 1, x, y))
                    visited.add((x, y))








