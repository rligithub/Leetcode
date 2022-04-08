class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[
        List[int]]:
        # 找出前k个解 使得grid[i][j] 在给定的范围内，res按distance排序，按price排序，按column排序
        m, n = len(grid), len(grid[0])
        heap = []
        heapq.heappush(heap, (0, grid[start[0]][start[1]], start[0], start[1]))
        visited = set()
        visited.add((start[0], start[1]))

        res = []
        while heap:
            dist, price, i, j = heapq.heappop(heap)
            if pricing[0] <= grid[i][j] <= pricing[1]:
                res.append([i, j])

            if len(res) == k:
                return res

            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid[x][y] > 0:
                    heapq.heappush(heap, (dist + 1, grid[x][y], x, y))
                    visited.add((x, y))
        return res