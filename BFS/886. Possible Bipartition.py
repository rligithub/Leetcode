class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # 和 #785 Is Graph Bipartite 一模一样，但是785 的node是从 0 ..n-1，而这道题是 1 ...n ，注意 padding 或者加一个额外空间
        # build graph #
        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        queue = collections.deque()
        color = [0] * (n + 1)

        for node in range(n):
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