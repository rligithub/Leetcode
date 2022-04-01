class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # step1: markdown each connected island as index , calculate area , save it in hashmap
        # step2: for loop each water to see if there are islands in the surroundings? if yes, new area = sum all + 1
        n = len(grid)
        hashmap = {}

        index = 2
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    hashmap[index] = self.bfs(grid, n, i, j, index)
                    index += 1
        res = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbors = set()
                    for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                        x = i + dx
                        y = j + dy
                        if 0 <= x < n and 0 <= y < n and grid[x][y] > 1:
                            neighbors.add(grid[x][y])
                    area = 1
                    for nei in neighbors:
                        area += hashmap[nei]
                    res = max(res, area)
        return res or n * n

    def bfs(self, grid, n, i, j, index):
        queue = collections.deque()
        queue.append((i, j))
        grid[i][j] = index

        count = 0
        while queue:
            i, j = queue.popleft()
            count += 1

            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                x = i + dx
                y = j + dy
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                    queue.append((x, y))
                    grid[x][y] = index

        return count
