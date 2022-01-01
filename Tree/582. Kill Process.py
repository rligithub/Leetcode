class Solution1:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        # BFS
        n = len(pid)
        hashmap = collections.defaultdict(list)  # {parent:child}
        for i in range(n):
            hashmap[ppid[i]].append(pid[i])

        res = []
        queue = collections.deque()
        queue.append(kill)

        while queue:
            cur = queue.popleft()
            res.append(cur)

            if cur in hashmap:
                for child in hashmap[cur]:
                    queue.append(child)
        return res


class Solution:  # DFS
    def killProcess(self, pid, ppid, kill):
        graph = collections.defaultdict(list)
        for p, pp in zip(pid, ppid):
            graph[pp].append(p)
        res = []
        self.dfs(graph, kill, res)
        return res

    def dfs(self, graph, node, res):

        res.append(node)
        for nei in graph[node]:
            self.dfs(graph, nei, res)


