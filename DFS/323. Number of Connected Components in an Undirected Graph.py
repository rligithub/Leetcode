class Solution1:
    def countComponents(self, n, edges):
        # same as #200 --> num of island
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        count = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                count += 1
                self.dfs(graph, i, visited)

        return count

    def dfs(self, graph, i, visited):
        visited.add(i)
        for nei in graph[i]:
            if nei not in visited:
                self.dfs(graph, nei, visited)




n = 5
edges = [[0,1],[0,2],[2,3],[2,4]]
a = Solution()
print(a.countComponents(n, edges))