class Solution:  # union find
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # return number of land cells that is not walkable from the boundary
        m, n = len(grid), len(grid[0])
        uf = UnionFind()
        # connect nodes with boundary
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                        uf.union(i * n + j, m * n)
                    for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                        x = i + dx
                        y = j + dy
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                            uf.union(i * n + j, x * n + y)
        print(uf.parent)
        # find nodes that not connect with boundary
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if uf.find(i * n + j) != m * n:
                        count += 1
        return count


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
            self.parent[min(rootA, rootB)] = max(rootA, rootB)
