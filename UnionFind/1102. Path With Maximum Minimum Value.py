class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        # smilar to swim in rising water

        positions = collections.defaultdict(set)
        m, n = len(grid), len(grid[0])
        start = (0, 0)
        end = (m - 1, n - 1)

        uf = UnionFind()

        for i in range(m):
            for j in range(n):
                positions[grid[i][j]].add((i, j))

        for height in sorted(positions.keys(), reverse=True):
            pos = positions[height]

            for (i, j) in pos:
                for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                    x = i + dx
                    y = j + dy
                    if 0 <= x < m and 0 <= y < n and grid[x][y] >= height:
                        uf.union((i, j), (x, y))

            if uf.find(start) == uf.find(end):
                return height


class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, i):
        if i not in self.parent:
            self.parent[i] = i

        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA != rootB:
            self.parent[rootA] = rootB