class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        uf = UnionFind()

        for i in range(m):
            for j in range(n):
                for dx, dy in (1, 0), (0, 1):
                    x = i + dx
                    y = j + dy
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == grid[i][j]:
                        if uf.find(i * n + j) == uf.find(x * n + y):
                            return True
                        uf.union(i * n + j, x * n + y)
        return False


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
