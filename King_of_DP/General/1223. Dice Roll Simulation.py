class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        # 摇色子， 同一个色子 连续摇出来的次数受限，求有多少种摇法
        memo = {}
        return self.dfs(rollMax, n, -1, 0, memo)

    def dfs(self, rollMax, n, cur, count, memo):
        if (n, cur, count) in memo:
            return memo[(n, cur, count)]

        mod = 10 ** 9 + 7

        if n == 0:
            return 1

        res = 0
        for i in range(6):
            if i != cur:
                res += self.dfs(rollMax, n - 1, i, 1, memo)
            elif count < rollMax[i]:
                res += self.dfs(rollMax, n - 1, i, count + 1, memo)

        memo[(n, cur, count)] = res % mod
        return memo[(n, cur, count)]