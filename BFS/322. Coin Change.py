class Solution2: # BFS
    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = collections.deque()
        queue.append((0, 0))
        visited = set()
        visited.add(0)

        while queue:
            summ, count = queue.popleft()
            if summ == amount:
                return count

            for c in coins:
                nxt_summ = summ + c
                if nxt_summ <= amount and nxt_summ not in visited:
                    queue.append((nxt_summ, count + 1))
                    visited.add(nxt_summ)

        return -1