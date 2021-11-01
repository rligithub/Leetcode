class Solution:
    def climbStairs(self, n: int) -> int:
        # 爬楼梯，每次可以爬 1 - 2层，求爬到顶的爬法
        memo = {}
        return self.dfs(n, memo)

    def dfs(self, n, memo):
        if n in memo:
            return memo[n]

        # BASE CASES --> n == 2, return 2; n == 1, return 1
        if n == 2:
            return 2
        if n == 1:
            return 1

        # TWO CASES: 每次爬一层 或者 每次爬两层
        memo[n] = self.dfs(n - 1, memo) + self.dfs(n - 2, memo)

        return memo[n]

