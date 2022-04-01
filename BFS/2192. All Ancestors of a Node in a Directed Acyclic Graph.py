class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # get a reverse graph --> children: parents
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[v].append(u)

        res = []
        for i in range(n):
            if i in graph:
                path = self.bfs(graph, i)
                res.append(sorted(path))
            else:
                res.append([])
        return res

    def bfs(self, graph, i):
        queue = collections.deque()
        queue.append(i)
        visited = set()
        visited.add(i)

        res = []
        while queue:
            node = queue.popleft()

            for nei in graph[node]:
                if nei not in visited:
                    queue.append(nei)
                    res.append(nei)
                    visited.add(nei)
        return res
