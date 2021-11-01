import math


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # n ge石头，每个人可以拿走x个（x非零，且为平方数），直到拿完为止，最后拿的人赢
        # memo -->
        memo = {}
        return self.dfs(n, memo)

    def dfs(self, n, memo):
        if n in memo:
            return memo[n]

        # 如果没有石头可以拿，先手就输了
        if n < 0:
            return False

        res = False
        for i in range(int(math.sqrt(n)), 0, -1):
            if n >= i * i and not self.dfs(n - i * i, memo):
                res = True
                break
        memo[n] = res
        return memo[n]
