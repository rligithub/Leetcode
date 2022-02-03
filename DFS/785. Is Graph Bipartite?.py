class Solution1:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # build graph #
        n = len(graph)
        color = {}

        for node in range(n):
            if node in color:
                continue
            color[node] = 0
            if not self.dfs(graph, color, node):
                return False
        return True

    def dfs(self, graph, color, node):

        for nei in graph[node]:
            if nei in color:
                if color[node] == color[nei]:
                    return False
            else:
                color[nei] = 1 - color[node]
                if not self.dfs(graph, color, nei):
                    return False
        return True


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # build graph #
        n = len(graph)
        colored = {}

        for node in range(n):
            if node not in colored:
                if not self.dfs(graph, colored, node, 1):
                    return False
        return True

    def dfs(self, graph, colored, node, color):
        if node in colored:
            return colored[node] == color

        colored[node] = color

        for nei in graph[node]:
            if not self.dfs(graph, colored, nei, color * (-1)):
                return False
        return True


