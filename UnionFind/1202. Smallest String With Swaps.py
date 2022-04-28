class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # swap后 smallest string是什么
        n = len(s)
        uf = UnionFind()

        # step1: union all index together
        for u, v in pairs:
            uf.union(u, v)

        # step2: build graph save swap_nodes --> {root_index: ch1, ch2}
        graph = collections.defaultdict(list)
        for i in range(n):
            root = uf.find(i)
            graph[root] += s[i]

        # step3: sort swap_nodes
        for swap_nodes in graph.values():
            swap_nodes.sort()

        # step4: for loop each index, find smallest char, append to res
        res = []
        for i in range(n):
            root = uf.find(i)
            ch = graph[root].pop(0)
            res.append(ch)
        return "".join(res)


class UnionFind:
    def __init__(self):
        self.parent = {}

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
