class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # union
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m * n)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                        x = i + dx
                        y = j + dy
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                            uf.union(i * n + j, x * n + y)

        # find + build graph to record size of connected lands
        count = collections.defaultdict(int)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    root = uf.find(i * n + j)
                    count[root] += 1
        # get max size
        res = 0
        for node in count:
            res = max(res, count[node])

        return res


class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA != rootB:
            self.parent[rootA] = rootB

