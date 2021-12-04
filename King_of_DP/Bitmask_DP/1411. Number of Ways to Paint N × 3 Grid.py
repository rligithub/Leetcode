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


class Solution2:  # bitmask - unknown
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


class Solution: # similar to happiness
    def numOfWays(self, n: int) -> int:
        memo = {}
        return self.dfs(n * 3, 0, 0, 0, 0, memo)

    def dfs(self, n, pos, red, yellow, green, memo):
        if (pos, red, yellow, green) in memo:
            return memo[(pos, red, yellow, green)]

        if pos == n:
            return 1

        row, col = pos // 3, pos % 3

        mod = 10 ** 9 + 7
        fullmask = (1 << 3) - 1

        nxt_red = (red << 1) & fullmask
        nxt_yellow = (yellow << 1) & fullmask
        nxt_green = (green << 1) & fullmask

        res = 0
        if self.valid(row, col, red):
            res += self.dfs(n, pos + 1, nxt_red + 1, nxt_yellow, nxt_green, memo)
        if self.valid(row, col, yellow):
            res += self.dfs(n, pos + 1, nxt_red, nxt_yellow + 1, nxt_green, memo)
        if self.valid(row, col, green):
            res += self.dfs(n, pos + 1, nxt_red, nxt_yellow, nxt_green + 1, memo)

        memo[(pos, red, yellow, green)] = res % mod
        return memo[(pos, red, yellow, green)]

    def valid(self, row, col, state):
        up = 1 << (3 - 1)

        if col == 0 and row == 0:
            return True

        if col > 0 and state & 1:  # has neighbor
            return False

        if row > 0 and state & up:  # has neighbor
            return False

        return True
a = Solution()
print(a.numOfWays(1))