class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # similar to num of island but with conditions

        m, n = len(grid2), len(grid2[0])
        count = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and (i, j) not in visited:
                    if self.dfs(grid2, m, n, grid1, i, j, visited):
                        count += 1

        return count

    def dfs(self, grid2, m, n, grid1, i, j, visited):
        # if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited or grid2[i][j] == 0:
        #     return True

        # if grid1[i][j] == 0 and grid2[i][j] == 1:
        #     return False

        res = grid1[i][j]

        visited.add((i, j))

        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            x = i + dx
            y = j + dy
            if 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid2[x][y] == 1:
                res &= self.dfs(grid2, m, n, grid1, x, y, visited)
        return res
