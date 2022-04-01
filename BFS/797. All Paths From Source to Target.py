class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        queue = collections.deque()
        queue.append((0, [0]))

        res = []
        while queue:
            cur, path = queue.popleft()
            if path and path[-1] == len(graph) - 1:
                res.append(path)
            for nxt in graph[cur]:
                queue.append((nxt, path + [nxt]))

        return res

