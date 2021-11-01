class Solution1:  # top down dp
    def canWinNim(self, n: int) -> bool:
        memo = {}
        return self.dfs(n, memo)

    def dfs(self, n, memo):
        # base case
        if n < 0:
            return False
        # check if in memo
        if n in memo:
            return memo[n]

        # initial
        res = False
        # if second players loss anyway == > we win
        for i in range(1, 4):
            if n - i >= 0 and not self.dfs(n - i, memo):
                res = True

        memo[n] = res
        return memo[n]


class Solution:  #
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0