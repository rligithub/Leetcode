class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # a和b不能在一个group，求能否将1..n分为两个parties
        # 和785. Is Graph Bipartite 一模一样
        # build graph #
        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

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


