class Solution3:  # UnionFind
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        uf = UnionFind(m * n)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    uf.count += 1
                    for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                        x = i + dx
                        y = j + dy
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                            uf.union(i * n + j, x * n + y)

        return uf.count


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.count = 0

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA != rootB:
            self.parent[min(rootA, rootB)] = max(rootA, rootB)
            self.count -= 1


class Solution:  # UnionFind
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        uf = UnionFind(m * n)

        # step1: UNION
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                        x = i + dx
                        y = j + dy
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                            uf.union(i * n + j, x * n + y)
        # step2: FIND
        res = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    root = uf.find(i * n + j)
                    if root not in visited:
                        visited.add(root)
                        res += 1
        return res


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA != rootB:
            self.parent[min(rootA, rootB)] = max(rootA, rootB)


