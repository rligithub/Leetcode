class Solution1:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)

        queue = collections.deque()
        visited = set()
        for i in range(n):
            queue.append((i, 1 << i, 0))
            visited.add((i, 1 << i))

        while queue:
            cur, mask, count = queue.popleft()
            if mask == (1 << n) - 1:
                return count

            for nxt in graph[cur]:
                nextmask = mask | (1 << nxt)
                if (nxt, nextmask) not in visited:
                    queue.append((nxt, nextmask, count + 1))
                    visited.add((nxt, nextmask))

        return 0


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        fullmask = (1 << n) - 1
        memo = {}

        res = float('inf')
        for node in range(n):
            res = min(res, self.dfs(graph, fullmask, node, memo))
        return res

    def dfs(self, graph, mask, node, memo):
        if (node, mask) in memo:
            return memo[(node, mask)]

        if mask & (mask - 1) == 0:
            return 0

        memo[(node, mask)] = float("inf")  # Avoid infinite loop in recursion

        for neighbor in graph[node]:
            if mask & (1 << neighbor):
                pick = 1 + self.dfs(graph, mask, neighbor, memo)
                not_pick = 1 + self.dfs(graph, mask ^ (1 << node), neighbor, memo)
                memo[(node, mask)] = min(memo[(node, mask)], pick, not_pick)

        return memo[(node, mask)]