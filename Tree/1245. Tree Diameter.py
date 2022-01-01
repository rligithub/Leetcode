class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        # max height and maxx height of two nodes --> each node return max height of child node
        if not edges:
            return 0

        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        self.res = float('-inf')

        self.dfs(graph, -1, 0)
        return self.res

    def dfs(self, graph, p, node):

        maxval1 = 0
        maxval2 = 0
        for child in graph[node]:
            if child != p:
                val = self.dfs(graph, node, child)
                if val > maxval1:
                    maxval2 = maxval1
                    maxval1 = val
                elif val > maxval2:
                    maxval2 = val

        self.res = max(self.res, maxval1 + maxval2)
        return maxval1 + 1


class Solution1:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0

        graph = collections.defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        self.res = 0
        self.visited = set()

        self.dfs(graph, 0)
        return self.res

    def dfs(self, graph, node):
        if node in self.visited:
            return 0

        self.visited.add(node)
        max_val = [0] * 2

        for nei in graph[node]:
            val = self.dfs(graph, nei)
            if val > min(max_val):
                max_val.remove(min(max_val))
                max_val.append(val)

        self.res = max(self.res, sum(max_val))
        return max(max_val) + 1