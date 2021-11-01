class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        # 给几个steps，可以向左走，向右走，不走，求有几种方式使得回到原点

        memo = {}
        return self.dfs(steps, arrLen, 0, memo)

    def dfs(self, steps, arrLen, pos, memo):
        if (pos, steps) in memo:
            return memo[(pos, steps)]

        if steps == 0:
            if pos == 0:
                return 1
            else:
                return 0

        mod = 10 ** 9 + 7

        left, right = 0, 0
        if pos - 1 >= 0:
            left = self.dfs(steps - 1, arrLen, pos - 1, memo)
        if pos + 1 <= arrLen - 1:
            right = self.dfs(steps - 1, arrLen, pos + 1, memo)

        stay = self.dfs(steps - 1, arrLen, pos, memo)

        memo[(pos, steps)] = (left + right + stay) % mod
        return memo[(pos, steps)]

