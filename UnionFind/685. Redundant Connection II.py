class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        # Return an edge that can be removed so that the resulting graph is a rooted tree of n nodes.

        n = len(edges)
        uf = UnionFind(n)

        # case1: if there is duplicate parents, record two edges as cand1 and cand2
        roots = {}
        cand1, cand2 = None, None
        for u, v in edges:
            if v in roots:
                cand1, cand2 = roots[v], [u, v]
                break
            roots[v] = [u, v]

        # case2: assum to delete cand2, for loop edges to see if there is cycle
        for u, v in edges:
            if [u, v] == cand2:  # skip cand2
                continue
            if uf.union(u,
                        v):  # has cycle --> if delete cand2 but there is still cycle, means cand1 is the one cause cycle
                if cand1:
                    return cand1
                return [u, v]
        return cand2


class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(1, n + 1)}

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            self.parent[rootA] = self.parent[rootB]
            return False  # no cycle
        return True  # has cycle





