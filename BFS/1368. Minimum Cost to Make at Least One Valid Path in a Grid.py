class Solution1:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        heap = []
        heapq.heappush(heap, (0, 0, 0))
        visited = set()

        while heap:
            cost, i, j = heapq.heappop(heap)
            if (i, j) in visited:
                continue
            visited.add((i, j))

            if i == m - 1 and j == n - 1:
                return cost

            for dx, dy, val in (1, 0, 3), (0, 1, 1), (-1, 0, 4), (0, -1, 2):
                x = i + dx
                y = j + dy
                if grid[i][j] == val:
                    new_cost = cost
                else:
                    new_cost = cost + 1
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                    heapq.heappush(heap, (new_cost, x, y))


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        heap = []
        heapq.heappush(heap, (0, 0, 0))
        memo = {}
        memo[(0, 0)] = 0

        while heap:
            cost, i, j = heapq.heappop(heap)

            if i == m - 1 and j == n - 1:
                return cost

            for dx, dy, val in (1, 0, 3), (0, 1, 1), (-1, 0, 4), (0, -1, 2):
                x = i + dx
                y = j + dy
                if grid[i][j] == val:
                    new_cost = cost
                else:
                    new_cost = cost + 1
                if 0 <= x < m and 0 <= y < n:
                    if (x, y) not in memo or new_cost < memo[(x, y)]:
                        heapq.heappush(heap, (new_cost, x, y))
                        memo[(x, y)] = new_cost

