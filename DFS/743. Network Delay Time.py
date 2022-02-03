class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 给一个指定的node k，求所有node都收到信号的最短总时间，如果不可能 则返回-1

        # step1: build graph
        graph = collections.defaultdict(list)
        for u, v, t in times:
            graph[u].append([t, v])

        time = {node: float('inf') for node in range(1, n + 1)}

        self.dfs(graph, k, time, 0)
        res = max(time.values())
        if res < float('inf'):
            return res
        return -1

    def dfs(self, graph, node, time, elapsed):
        if elapsed >= time[node]:
            return
        time[node] = elapsed

        for t, nei in sorted(graph[node]):
            self.dfs(graph, nei, time, elapsed + t)

