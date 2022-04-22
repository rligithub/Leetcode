class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 找出circle在的点--> return the egdes that occurs last in the input
        # no repeat edges
        n = len(edges)  # num of nodes
        uf = UnionFind(n)

        for u, v in edges:
            if uf.union(u, v):  # if cycle
                return [u, v]


class UnionFind():
    def __init__(self, n):
        self.parent = {i: i for i in range(1, n + 1)}  # node from 1...n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA != rootB:
            self.parent[rootA] = rootB
            return False  # no cycle
        return True  # has cycle
