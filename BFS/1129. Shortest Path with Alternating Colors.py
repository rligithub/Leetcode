class Solution1:  # TLE
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # build graph for rededges and bluedges --> alternately 正负来表示

        graph = collections.defaultdict(list)

        for u, v in redEdges:
            graph[u].append(v)
        for u, v in blueEdges:
            graph[-u].append(-v)
        # for loop nodes --> bfs find the shortest path from node 0 to node
        res = []
        for i in range(n):
            step = self.bfs(graph, i, n)
            res.append(step)
        return res

    def bfs(self, graph, i, n):
        queue = collections.deque()
        queue.append((0, 0))

        while queue:
            node, step = queue.popleft()
            if abs(node) == i:
                return step

            for nei in graph[-node]:
                queue.append((nei, step + 1))

        return -1


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # build graph for rededges and bluedges --> alternately 正负来表示

        graph = collections.defaultdict(list)

        for u, v in redEdges:
            graph[u].append((v, 1))
        for u, v in blueEdges:
            graph[u].append((v, -1))
        # update step in each node --> bfs find the shortest path from node 0 to node
        res = [-1] * n

        queue = collections.deque()
        queue.append((0, 'inf'))
        visited = set()
        visited.add(0)

        step = 0
        while queue:
            size = len(queue)
            for i in range(size):
                node, color = queue.popleft()
                if res[node] == -1:
                    res[node] = step
                for nei, nei_color in graph[node]:
                    if nei_color != color and (nei, nei_color) not in visited:
                        queue.append((nei, nei_color))
                        visited.add((nei, nei_color))
            step += 1
        return res



