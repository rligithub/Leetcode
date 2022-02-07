class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # see if source node is connected to destination node
        # step1: build graph
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # step2: check if two nodes are connected --> if destination is in source node's neighbors
        visited = set()
        return self.dfs(graph, source, destination, visited)

    def dfs(self, graph, start, end, visited):
        if start == end:
            return True

        visited.add(start)

        for nei in graph[start]:
            if nei not in visited:
                if self.dfs(graph, nei, end, visited):
                    return True

        return False