"""

n = 1
k
n = 2
same = k
diff = k * (k-1)
k + k * (k-1) = k * k


dfs(i) = same(i) + diff(i)

diff(i) = dfs(i-1) * (k-1)
same(i) = diff(i-1) =

dfs(i) = dfs(i-2) * (k-1) + dfs(i-1) * (k-1)

dfs(i) = (dfs(i-2) + dfs(i-1)) * (k-1) * (k-1)

"""


class Solution1:
    def numWays(self, n: int, k: int) -> int:
        memo = {}
        return self.dfs(n, k, memo)

    def dfs(self, n, k, memo):
        if (n, k) in memo:
            return memo[(n, k)]

        if n == 1:
            return k

        if n == 2:
            return k * k

        memo[(n, k)] = (self.dfs(n - 2, k, memo) + self.dfs(n - 1, k, memo)) * (k - 1)
        return memo[(n, k)]


class Solution:
    def numWays(self, n: int, k: int) -> int:

        memo = {}

        return self.dfs(n, k, -1, False, memo)

    def dfs(self, n, k, prev, lastTwoSame, memo):
        if (n, lastTwoSame) in memo:
            return memo[(n, lastTwoSame)]

        if n == 0:
            return 1

        res = 0
        for color in range(k):
            if color == prev and lastTwoSame:
                continue
            res += self.dfs(n - 1, k, color, color == prev, memo)

        memo[(n, lastTwoSame)] = res
        return memo[(n, lastTwoSame)]







