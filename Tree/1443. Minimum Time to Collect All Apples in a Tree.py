class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # build graph + DFS + backtracking + apples_num -- + return steps

        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        self.res = 0
        self.dfs(graph, hasApple, visited, 0)
        return self.res

    def dfs(self, graph, hasApple, visited, node):
        if node not in graph:
            return 0

        visited.add(node)
        step = 0

        for nei in graph[node]:
            if nei not in visited:
                if self.dfs(graph, hasApple, visited, nei) > 0 or hasApple[nei]:
                    step += 2
        self.res += step
        return step


