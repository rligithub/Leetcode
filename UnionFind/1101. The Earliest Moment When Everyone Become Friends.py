class Solution1:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        # 求 所有的人都成为好朋友的最短时间 最后只能剩下一个group
        uf = UnionFind(n)
        logs = sorted(logs)

        for time, u, v in logs:
            if uf.find(u) != uf.find(v):
                uf.union(u, v)
            if uf.count == 1:
                return time
        return -1


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


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        # 求 所有的人都成为好朋友的最短时间 --> 看 联通在一起几个人 是不是为 n
        uf = UnionFind()
        logs = sorted(logs)

        for time, u, v in logs:
            if uf.find(u) != uf.find(v):
                uf.union(u, v)
            if uf.count == n - 1:
                return time
        return -1


class UnionFind:
    def __init__(self):
        self.parent = {}
        self.count = 0

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
            self.count += 1