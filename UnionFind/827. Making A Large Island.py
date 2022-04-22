class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # step1: union all lands togethers
        # step2: find --> if the same root, count ++ ---> counts[root] = size of each lands
        # step3: for loop each water to see if there are islands in the surroundings? if yes, new area = sum all + 1
        n = len(grid)
        uf = UnionFind(n * n)

        # step1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                        x = i + dx
                        y = j + dy
                        if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                            uf.union(i * n + j, x * n + y)

        # step2
        counts = collections.defaultdict(int)
        for i in range(n * n):
            root = uf.find(i)
            counts[root] += 1

        # step3
        res = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbors = set()
                    for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                        x = i + dx
                        y = j + dy
                        if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                            root = uf.find(x * n + y)
                            neighbors.add(root)
                    area = 1
                    for root in neighbors:
                        area += counts[root]
                    res = max(res, area)
        return res or n * n


class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(n + 1)}

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA != rootB:
            self.parent[rootA] = rootB