class Solution:  # BFS
    def killProcess(self, pid, ppid, kill):
        # build graph
        graph = collections.defaultdict(list)
        for i, p in enumerate(ppid):
            graph[p].append(pid[i])

        queue = collections.deque()
        queue.append(kill)
        res = []

        while queue:
            node = queue.popleft()
            res.append(node)

            for nei in graph[node]:
                queue.append(nei)
        return res