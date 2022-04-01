class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, t in flights:
            graph[u].append([v, t])

        queue = collections.deque()
        queue.append((src, 0, 0))
        memo = {}  # 不同处
        memo[src] = 0
        res = float('inf')
        while queue:
            cur, time, count = queue.popleft()
            if cur == dst and count <= k + 1:
                res = min(res, time)
            for nei, t in graph[cur]:
                new_time = time + t
                if nei not in memo or new_time < memo[nei]:  # 不同处
                    memo[nei] = new_time
                    queue.append([nei, new_time, count + 1])
        if res < float('inf'):
            return res
        return -1
