class Solution1:
    def numOfWays(self, n: int) -> int:
        memo = {}
        return self.dfs(n * 3, 0, 0, 0, memo)

    def dfs(self, n, pprev, prev, cur, memo):
        if (n, pprev, prev, cur) in memo:
            return memo[(n, pprev, prev, cur)]

        if n == 0:
            return 1

        mod = 10 ** 9 + 7

        res = 0
        for nxt in (1, 2, 3):
            if (nxt != pprev and (nxt != cur or n % 3 == 0)):
                res += self.dfs(n - 1, prev, cur, nxt, memo)

        memo[(n, pprev, prev, cur)] = res % mod
        return memo[(n, pprev, prev, cur)]


class Solution:  # bitmask - unknown
    def numOfWays(self, n: int) -> int:
        memo = {}
        return self.dfs(n * 3, 0, memo)

    def dfs(self, n, state, memo):
        if (n, state) in memo:
            return memo[(n, state)]

        if n == 0:
            return 1

        mod = 10 ** 9 + 7

        res = 0
        pprev = state & 48
        prev = state & 12
        cur = state & 3

        for nxt in (1, 2, 3):
            if (nxt != pprev >> 4 and (nxt != cur or n % 3 == 0)):
                res += self.dfs(n - 1, (prev | cur) << 2 | nxt, memo)

        memo[(n, state)] = res % mod
        return memo[(n, state)]


