class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # construct a hashmap --> {height: (i, j)}
        positions = collections.defaultdict(set)
        n = len(grid)
        start = (0, 0)
        end = (n - 1, n - 1)

        uf = UnionFind()

        for i in range(n):
            for j in range(n):
                positions[grid[i][j]].add((i, j))

        # for each height value, merge with each neighboring cell if neighbor also has <= height value
        for height in sorted(positions.keys()):
            pos = positions[height]

            for (i, j) in pos:
                for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                    x = i + dx
                    y = j + dy
                    if 0 <= x < n and 0 <= y < n and grid[x][y] <= height:
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
