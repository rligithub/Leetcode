class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # similar to num of islands

        uf = UnionFind(n)
        # for loop node, count ++, union count --
        for u, v in edges:
            uf.union(u, v)

        return uf.count + n  # for loop n node, each time union together --


class UnionFind():
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
