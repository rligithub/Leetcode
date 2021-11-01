class Solution1:  # TLE
    def findDerangement(self, n: int) -> int:
        # 给一组数，给他们重新换位置，每个数不能在原先的位置，求有几种换法
        # ending point ---> pos == n
        # swap two numbers

        memo = {}
        return self.dfs(n, memo)

    def dfs(self, n, memo):
        if n in memo:
            return memo[n]

        mod = 10 ** 9 + 7

        if n == 0:
            return 1

        res = 0
        for x in range(n - 1):
            swap = self.dfs(n - 2, memo)
            not_swap = self.dfs(n - 1, memo)
            res += swap + not_swap

        memo[n] = res % mod
        return memo[n]


class Solution:  # bottom up dp
    def findDerangement(self, n: int) -> int:
        mod = 10 ** 9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 0

        for i in range(2, n + 1):
            dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2]) % mod

        return dp[-1]