class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        self.res = [0] * n

        self.dfs(0, labels, graph)

        return self.res

    def dfs(self, root, labels, graph):
        count = collections.Counter()

        for nei in graph[root]:
            graph[nei].remove(root)
            count += self.dfs(nei, labels, graph)

        count[labels[root]] += 1
        self.res[root] = count[labels[root]]

        return count