class Solution:  # union find
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # graph {node: neighbor nodes}
        n = len(graph)

        # find to see if in the same group --> if not, union all neighbors together
        uf = UnionFind(n)
        for i in range(n):
            for j in graph[i]:
                if uf.find(i) == uf.find(j):
                    return False
                uf.union(j, graph[i][0])
        return True


class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])

        return self.parent[i]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA != rootB:
            self.parent[rootA] = rootB