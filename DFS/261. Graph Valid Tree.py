class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # all nodes are used + no circle
        graph = collections.defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        return self.dfs(graph, 0, -1, visited) and len(visited) == n

    def dfs(self, graph, node, parent, visited):

        if node in visited:
            return False
        visited.add(node)

        for nei in graph[node]:
            if nei != parent:
                if not self.dfs(graph, nei, node, visited):
                    return False
        return True

