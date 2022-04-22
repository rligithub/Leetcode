class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # 和 #785 Is Graph Bipartite 一模一样，但是785 的node是从 0 ..n-1，而这道题是 1 ...n ，注意 padding 或者加一个额外空间
        # 并查集，一般只进行连“连接”操作，而本题的题意是要“断开”

        uf = UnionFind(n)
        # build graph {p: dislike ppl}
        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        for i in range(1, n + 1):
            for j in graph[i]:  # 与当前节点连接的节点不能在一个集合中 -- to make sure dislike ppl not in the same group
                if uf.find(i) == uf.find(j):
                    return False
                uf.union(j, graph[i][0])  # 连接当前节点的所有的邻居节点，这些邻居节点必须在一个集合 --> to union all dislike ppl together
        return True


class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(1, n + 1)}

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA != rootB:
            self.parent[rootA] = rootB
