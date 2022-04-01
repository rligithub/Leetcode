import heapq
class Solution:  # BFS + heap --> visited用set来表示
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # graph = collections.defaultdict(dict)
        # for u, v, w in times:
        #     graph[u][v] = w

        graph = collections.defaultdict(list)
        for u, v, t in times:
            graph[u].append([v, t])

        heap = []
        heapq.heappush(heap, ((0, k)))
        visited = set()
        res = float('inf')
        while heap:
            time, cur = heapq.heappop(heap)
            if cur in visited:
                continue
            visited.add(cur)
            if len(visited) == n:
                res = min(res, time)
            for nei, t in graph[cur]:
                new_time = time + t
                heapq.heappush(heap, ((new_time, nei)))

        if res < float('inf'):
            return res
        return -1


class Solution2:  # BFS --> memo，开一个固定大小
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = collections.defaultdict(list)
        for u, v, t in times:
            graph[u].append([v, t])

        queue = collections.deque()
        queue.append((k, 0))
        memo = {node: -1 for node in range(1, n + 1)}  # 不同处
        memo[k] = 0

        while queue:
            cur, time = queue.popleft()
            for nei, t in graph[cur]:
                new_time = time + t
                if memo[nei] == -1 or new_time < memo[nei]:  # 不同处
                    memo[nei] = new_time
                    queue.append([nei, new_time])
        res = -1
        for i in range(1, n + 1):
            if memo[i] == -1:  # 不同处
                return -1
            res = max(res, memo[i])
        return res


class Solution3:  # BFS --> memo用dictionary来表示，不用开一个固定大小
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = collections.defaultdict(list)
        for u, v, t in times:
            graph[u].append([v, t])

        queue = collections.deque()
        queue.append((k, 0))
        memo = {}  # 不同处
        memo[k] = 0

        while queue:
            cur, time = queue.popleft()
            for nei, t in graph[cur]:
                new_time = time + t
                if nei not in memo or new_time < memo[nei]:  # 不同处
                    memo[nei] = new_time
                    queue.append([nei, new_time])
        res = -1
        for i in range(1, n + 1):
            if i not in memo:  # 不同处
                return -1
            res = max(res, memo[i])
        return res


