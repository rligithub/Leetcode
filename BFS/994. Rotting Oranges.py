class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # step1: append rotten orange + count num of fresh and rotten orange
        # step2: make all fresh orange rotten -- > stop when len(visited) == orange_count, return step

        m, n = len(grid), len(grid[0])
        queue = collections.deque()
        visited = set()

        orange_count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    orange_count += 1

        if orange_count == 0:
            return 0

        res = -1
        while queue:
            i, j, minute = queue.popleft()

            if len(visited) == orange_count:
                res = max(res, minute)

            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid[x][y] == 1:
                    queue.append((x, y, minute + 1))
                    visited.add((x, y))

        return res

