class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        uf = UnionFind()
        n = len(source)

        # step: union all index together
        for u, v in allowedSwaps:
            uf.union(u, v)

        # step2: build graph save swap_nodes --> {index: ch1, ch2}
        graph = collections.defaultdict(collections.Counter)

        for i in range(len(source)):
            root = uf.find(i)
            graph[root][source[i]] += 1
        print(graph)

        count = 0
        for i in range(n):
            num = target[i]
            p = uf.find(i)

            if graph[p][num] > 0:
                graph[p][num] -= 1
            else:
                count += 1
        return count


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

