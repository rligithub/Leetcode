class Solution1:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        neighbors = collections.defaultdict(list)
        for u, v in edges:
            neighbors[v].append(u)
            neighbors[u].append(v)

        self.count = [1] * n
        self.dist = [0] * n
        # find node 0 to all others dist
        self.dfs1(neighbors, 0, None)

        # find all other node except for 0, to all others dist
        self.dfs2(neighbors, n, 0, None)

        return self.dist

    def dfs1(self, neighbors, node, parent):
        for child in neighbors[node]:
            if child != parent:
                self.dfs1(neighbors, child, node)

                self.count[node] += self.count[child]
                self.dist[node] += self.dist[child] + self.count[child]

    def dfs2(self, neighbors, n, node, parent):
        for child in neighbors[node]:
            if child != parent:
                self.dist[child] = self.dist[node] - self.count[child] + (n - self.count[child])

                self.dfs2(neighbors, n, child, node)