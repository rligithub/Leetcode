class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        uf = UnionFind(n)
        for u, v in edges:
            if uf.union(u, v):  # if has cycle
                return False
        return True


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
            return False  # no cycle
        return True  # has cycle