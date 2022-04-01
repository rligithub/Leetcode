class Solution:  # BFS
    def numSquares(self, n: int) -> int:
        queue = collections.deque()
        queue.append((0, 0)) # 初始值 只能为 0
        visited = set()
        visited.add(0)

        while queue:
            summ, level = queue.popleft()
            if summ == n:
                return level
            for num in range(int(math.sqrt(n)), 0, -1):
                nxt_summ = summ + num**2
                if nxt_summ <= n and nxt_summ not in visited:
                    visited.add(nxt_summ)
                    queue.append((nxt_summ,level+1))
