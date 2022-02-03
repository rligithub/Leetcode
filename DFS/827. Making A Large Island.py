class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # 找连续的'1'的最大面积，可以将一个'0'变为'1'

        n = len(grid)

        land = {}
        index = 2

        # step1: markdown each connected island as index , calculate area , save it in hashmap
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    land[index] = self.dfs(grid, n, i, j, index)  # area of island x
                    index += 1

        # step2: for loop each water to see if there are islands in the surroundings? if yes, new area = sum all + 1
        res = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:  # water
                    neighbors = set()
                    for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                        x = i + dx
                        y = j + dy
                        if 0 <= x < n and 0 <= y < n and grid[x][y] > 1:  # there are islands for water[i, j]
                            neighbors.add(grid[x][y])
                    areas = 0
                    for nei in neighbors:
                        areas += land[nei]
                    res = max(res, areas + 1)

        return res or n * n  # if no water and all islands --> return n*n

    def dfs(self, grid, n, i, j, index):
        area = 0
        if 0 <= i < n and 0 <= j < n and grid[i][j] == 1:
            grid[i][j] = index
            area += 1
            area += self.dfs(grid, n, i + 1, j, index)
            area += self.dfs(grid, n, i - 1, j, index)
            area += self.dfs(grid, n, i, j + 1, index)
            area += self.dfs(grid, n, i, j - 1, index)
        return area




