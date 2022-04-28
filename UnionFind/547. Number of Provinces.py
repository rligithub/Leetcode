class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # how many connected provinces
        n = len(isConnected)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    uf.union(i, j)

        return uf.count


class UnionFind():
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
            self.parent[min(rootA, rootB)] = max(rootA, rootB)
            self.count -= 1