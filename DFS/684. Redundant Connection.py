class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 找出circle在的点--> return the egdes that occurs last in the input

        # step1: build graph
        graph = collections.defaultdict(list)
        res = []

        for u, v in edges:
            if self.dfs(graph, u, v, set()):
                return [u, v]
            graph[u].append(v)
            graph[v].append(u)
        return res

    def dfs(self, graph, x, y, visited):
        if x == y:
            return True

        visited.add(x)
        for nei in graph[x]:
            if nei not in visited:
                if self.dfs(graph, nei, y, visited):
                    return True



