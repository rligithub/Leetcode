class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # num of islands ---> 最多删掉几个 ---> 即 总共的点 - 总共的块数（每块剩一个）
        n = len(stones)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    uf.union(i, j)

        return - uf.count


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
            self.count -= 1

