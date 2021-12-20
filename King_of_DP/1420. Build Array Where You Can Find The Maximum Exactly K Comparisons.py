class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        # 给一个程序，这个程序用来找一个数组中的最大值，每更新一次最大值cost++，求给一个最大值m和cost k，有几种方式组成这个数组

        memo = {}
        return self.dfs(n, m, k, -1, memo)

    def dfs(self, n, m, k, cur, memo):
        if (n, k, cur) in memo:
            return memo[(n, k, cur)]

        if n == 0:
            if k == 0:
                return 1
            else:
                return 0

        mod = 10 ** 9 + 7

        res = 0
        for i in range(1, m + 1):
            if i > cur:
                res += self.dfs(n - 1, m, k - 1, i, memo)
            else:
                res += self.dfs(n - 1, m, k, cur, memo)

        memo[(n, k, cur)] = res % mod
        return memo[(n, k, cur)]