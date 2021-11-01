class Solution1:  # TLE
    def numberOfSets(self, n: int, k: int) -> int:
        memo = {}
        return self.dfs(n, k, memo)

    def dfs(self, n, k, memo):
        if (n, k) in memo:
            return memo[(n, k)]

        if k >= n:
            return 0
        if k == 1:
            return n * (n - 1) // 2
        if k == n - 1:
            return 1
        mod = 10 ** 9 + 7

        res = 0
        for i in range(2, n - k + 2):
            res += self.dfs(n - i + 1, k - 1, memo) * (i - 1)

        memo[(n, k)] = res % mod
        return memo[(n, k)]


class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        memo = {}
        return self.dfs(n, 0, k, True, memo)

    def dfs(self, n, pos, k, is_start, memo):
        if (pos, k, is_start) in memo:
            return memo[(pos, k, is_start)]

        if k == 0:
            return 1
        if pos == n:
            return 0

        mod = 10 ** 9 + 7

        # if not pick this point, skip
        not_pick = self.dfs(n, pos + 1, k, is_start, memo)

        pick = 0
        # TWO CASES: if the point can be a start point
        # if it is start point --> next point is not start point , pos ++
        # if not a start point --> next point must be a start point, pos can be next point's start point
        if is_start:
            pick += self.dfs(n, pos + 1, k, False, memo)
        else:
            pick += self.dfs(n, pos, k - 1, True, memo)

        memo[(pos, k, is_start)] = (not_pick + pick) % mod
        return memo[(pos, k, is_start)]







