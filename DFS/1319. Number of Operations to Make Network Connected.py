import collections

class Solution:
    def makeConnected(self, n: int, connections) -> int:
        # similar to num of islands --> get edges needed --> num of nodes - 1

        # n 个 nodes 最少需要 n - 1 edges
        # edge cases
        if len(connections) < n - 1:
            return -1

        graph = collections.defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                self.dfs(graph, i, visited)
                count += 1
        return count - 1

    def dfs(self, graph, i, visited):
        visited.add(i)
        for nei in graph[i]:
            if nei not in visited:
                self.dfs(graph, nei, visited)