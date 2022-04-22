class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # similar to num of islands --> get edges needed --> num of nodes - 1
        if len(connections) < n - 1:
            return -1
        uf = UnionFind(n)
        for u, v in connections:
            uf.union(u, v)

        return uf.count - 1


class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.count = n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA != rootB:
            self.parent[rootA] = rootB
            self.count -= 1
