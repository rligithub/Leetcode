class Solution1:  # dfs
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        # return left uper corner and right bottom right corner for each group land

        m, n = len(land), len(land[0])

        res = []
        visited = set()
        for i in range(m):
            for j in range(n):
                self.maxx = i
                self.maxy = j
                if land[i][j] == 1 and (i, j) not in visited:
                    self.dfs(land, m, n, i, j, visited)
                    res.append([i, j, self.maxx, self.maxy])
        return res

    def dfs(self, land, m, n, i, j, visited):

        visited.add((i, j))
        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            x = i + dx
            y = j + dy
            if 0 <= x < m and 0 <= y < n and (x, y) not in visited and land[x][y] == 1:
                self.maxx = max(self.maxx, x)
                self.maxy = max(self.maxy, y)
                self.dfs(land, m, n, x, y, visited)


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])

        res = []
        for i in range(m):
            for j in range(n):
                self.search(land, m, n, i, j, res)

        return res

    def search(self, land, m, n, i, j, res):
        if land[i][j] == 1:
            x = i
            y = j
            # farmland area is rectangle
            while x < m and land[x][j] == 1:
                x += 1
            while y < n and land[i][y] == 1:
                y += 1

            # marked land as visited
            for c in range(i, x):
                for r in range(j, y):
                    land[c][r] = 0

            res.append([i, j, x - 1, y - 1])
