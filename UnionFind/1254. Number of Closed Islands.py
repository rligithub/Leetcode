class Solution:  # union find
    def closedIsland(self, grid: List[List[int]]) -> int:
        # num of island that not connected with 边边
        uf = UnionFind()

        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                        uf.union(i * n + j, m * n)
                    for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                        x = i + dx
                        y = j + dy
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == 0:
                            uf.union(i * n + j, x * n + y)

        visited = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    root = uf.find(i * n + j)
                    if root != m * n and root not in visited:
                        visited.add(root)
        return len(visited)


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
