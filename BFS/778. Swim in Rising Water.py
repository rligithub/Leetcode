class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # bfs
        m, n = len(grid), len(grid[0])
        heap = []
        heapq.heappush(heap, (grid[0][0], 0, 0))
        visited = set()
        visited.add((0, 0))

        res = 0
        while heap:
            height, i, j = heapq.heappop(heap)
            res = max(res, height)

            if i == m - 1 and j == n - 1:
                return res

            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                    visited.add((x, y))
                    heapq.heappush(heap, (grid[x][y], x, y))
