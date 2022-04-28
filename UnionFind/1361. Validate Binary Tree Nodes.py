class Solution3:  # UnionFind
    def validateBinaryTreeNodes(self, n, left, right):
        uf = UnionFind(n)
        indegree = collections.defaultdict(int)

        for i in range(n):
            if left[i] != -1:
                indegree[left[i]] += 1
                uf.union(left[i], i)

            if right[i] != -1:
                indegree[right[i]] += 1
                uf.union(right[i], i)

        p = 0
        for node in indegree:
            if indegree[node] > 1:  # each node can only have 1 parent
                return False
            p += indegree[node]
        return p == n - 1 and uf.count == 1  # valid tree --> all has parents + all are connected as one group


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
