class Solution:  # BFS + BFS
    def shortestBridge(self, grid):

        m, n = len(grid), len(grid[0])
        queue1 = collections.deque()
        queue2 = collections.deque()

        # step1: find the first point which grid[i][j] == 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row, column = i, j
                    break

                    # step2: put all lands in first island into queue
        self.bfs1(queue1, queue2, grid, m, n, row, column)

        # step3: search surrounding to see if there is second island, each time ++
        return self.bfs2(queue2, grid, m, n)

    def bfs1(self, queue1, queue2, grid, m, n, i, j):
        queue1.append((i, j))
        grid[i][j] = 2
        queue2.append([i, j])

        while queue1:
            i, j = queue1.popleft()
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    grid[x][y] = 2
                    queue1.append((x, y))
                    queue2.append([x, y])

    def bfs2(self, queue, grid, m, n):
        res = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()

                for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    x = i + dx
                    y = j + dy

                    if x < 0 or x >= m or y < 0 or y >= n:
                        continue
                    if grid[x][y] == 0:
                        grid[x][y] = 3
                        queue.append([x, y])
                    elif grid[x][y] == 1:
                        return res
            res += 1
