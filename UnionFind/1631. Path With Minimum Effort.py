class Solution:  # union find
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # step1: build graph --> [height_diff, (i, j), (x, y)]
        m, n = len(heights), len(heights[0])
        if n == 1 and m == 1:
            return 0

        uf = UnionFind()
        start = (0, 0)
        end = (m - 1, n - 1)

        graph = []
        for i in range(m):
            for j in range(n):
                for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                    x = i + dx
                    y = j + dy
                    if 0 <= x < m and 0 <= y < n:
                        diff = abs(heights[i][j] - heights[x][y])
                        graph.append([diff, (i, j), (x, y)])
        # step2: sorted graph
        graph = sorted(graph, key=lambda x: x[0])

        # step3: union all points to see if start and end are connected
        for diff, first, second in graph:
            (i, j) = first
            (x, y) = second
            if uf.find((i, j)) != uf.find((x, y)):
                uf.union((i, j), (x, y))
            if uf.find(start) == uf.find(end):
                return diff


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
