class SolutionTLE:  # TLE
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        # union
        uf = UnionFind()

        for i in range(1, n):
            for j in range(i + 1, n + 1):
                if self.commonDivisor(i, j, threshold, n):
                    uf.union(i, j)

        # for loop queries to check if u and v are connected
        res = []
        for u, v in queries:
            res.append(uf.find(u) == uf.find(v))
        return res

    def commonDivisor(self, a, b, threshold, n):
        for div in range(threshold + 1, n + 1):
            if a % div == 0 and b % div == 0:
                return True
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


class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        # union
        uf = UnionFind()

        for i in range(threshold + 1, n):
            for j in range(2 * i, n + 1, i):
                uf.union(i, j)

        # for loop queries to check if u and v are connected
        res = []
        for u, v in queries:
            res.append(uf.find(u) == uf.find(v))
        return res


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