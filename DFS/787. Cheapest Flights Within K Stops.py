class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(dict)
        for fr, to, cost in flights:
            graph[fr][to] = cost

        memo = {}

        res = self.dfs(graph, src, dst, k + 1, memo)
        if res < float('inf'):
            return res
        return -1

    def dfs(self, graph, start, end, k, memo):
        if (start, k) in memo:
            return memo[(start, k)]
        if start == end:
            return 0
        if k == 0:
            return float('inf')

        res = float('inf')
        for nei in graph[start].keys():
            res = min(res, self.dfs(graph, nei, end, k - 1, memo) + graph[start][nei])

        memo[(start, k)] = res
        return res

