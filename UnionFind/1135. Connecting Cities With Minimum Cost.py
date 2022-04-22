class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        # 最后变成一个group
        uf = UnionFind(n)

        connections = sorted(connections, key=lambda x: x[2])

        res = 0
        for u, v, cost in connections:
            if uf.find(u) != uf.find(v):
                uf.union(u, v)
                res += cost
            if uf.count == 1:
                return res
        return -1


class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(1, n + 1)}
        self.count = n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA != rootB:
            self.parent[min(rootA, rootB)] = max(rootA, rootB)
            self.count -= 1