class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        queue = collections.deque()
        color = [0] * len(graph)

        for node in range(len(graph)):
            if color[node] != 0:
                continue
            if not self.bfs(graph, color, queue, node):
                return False
        return True

    def bfs(self, graph, color, queue, node):
        queue.append((node, -1))
        while queue:
            node, c = queue.popleft()
            color[node] = c

            for nei in graph[node]:
                if color[nei] == color[node]:
                    return False
                if color[nei] == 0:
                    queue.append((nei, c * (-1)))

        return True

