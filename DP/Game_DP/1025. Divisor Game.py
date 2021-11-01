class Solution:  # top down dp
    def divisorGame(self, n: int) -> bool:
        # 每个人可以在 n 中选数字x（x大于0小于n 并且 x能被n整除），下一个人从 n-x 中选数字，直到选不出x为止（即 n == 1）
        memo = {}
        return self.dfs(n, memo)

    def dfs(self, n, memo):
        if n in memo:
            return memo[n]

        if n == 1:
            return False

        res = False
        for x in range(1, n // 2 + 1):
            if n % x == 0 and not self.dfs(n - x, memo):
                res = True
                break
        memo[n] = res
        return memo[n]