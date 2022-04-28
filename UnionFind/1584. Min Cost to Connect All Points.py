class Solution:  # faster
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # step1: calculate distance between each two points
        n = len(points)
        if n == 0 or n == 1:
            return 0

        graph = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph.append((i, j, dist))

        # step2: sort graph by distance
        graph = sorted(graph, key=lambda x: x[2])

        uf = UnionFind(n)
        # step3: union all points to see if are points are connected --> uf.count == 1
        res = 0
        for i, j, dist in graph:
            if uf.find(i) != uf.find(j):
                uf.union(i, j)
                res += dist
            if uf.count == 1:
                return res


class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.count = n

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
            self.count -= 1


class Solution1:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # step1: calculate distance between each two points
        n = len(points)
        if n == 0 or n == 1:
            return 0

        graph = []
        for first in points:
            for second in points:
                if first != second:
                    dist = abs(first[0] - second[0]) + abs(first[1] - second[1])
                    graph.append(((first[0], first[1]), (second[0], second[1]), dist))

        # step2: sort graph by distance
        graph = sorted(graph, key=lambda x: x[2])

        uf = UnionFind(n)
        # step3: union all points to see if are points are connected --> uf.count == 1
        res = 0
        for first, second, dist in graph:
            if uf.find(first) != uf.find(second):
                uf.union(first, second)
                res += dist
            if uf.count == 1:
                return res


class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.count = n

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
            self.count -= 1
