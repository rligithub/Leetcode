class Solution:  # Union Find
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        uf = UnionFind(n)

        for i in range(0, n, 2):
            uf.union(row[i] // 2, row[i + 1] // 2) # 把相邻couple的座位调出来，连接他们的座位
        return uf.count


class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.count = 0

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA != rootB:
            self.parent[rootA] = rootB
            self.count += 1     # 找出有几个连接的座位，即 有几个需要swap
