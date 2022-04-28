class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # 求可以删除的最大边数，等同于用最少的边构建Alice和Bob可以完全遍历的图

        # step1: 构建两个并查集parents1，parents2对应Alice和Bob
        uf1, uf2 = UnionFind(n), UnionFind(n)
        res = 0

        # step2: 第一次遍历edges：只用类型3的边构建图，同时计数类型3多余的边；
        # 公共边
        for t, u, v in edges:
            if t == 3:
                if uf1.union(u, v):  # has cycle, 需要合并的两个点属于同一个连通分量，那么就说明当前这条边可以被删除，将答案增加 11
                    res += 1
                else:
                    uf2.union(u, v)
        # step3: 第二次遍历edges：只用类型1和类型2的边构建图，同时计数这两种类型多余的边
        # 独占边
        for t, u, v in edges:
            if t == 1:
                # Alice 独占边
                if uf1.union(u, v):  # has cycle
                    res += 1
            elif t == 2:
                # Bob 独占边
                if uf2.union(u, v):  # has cycle
                    res += 1

        if uf1.count == 1 and uf2.count == 1:
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
            self.parent[rootA] = rootB
            self.count -= 1
            return False  # no cycle
        return True  # has cycle
