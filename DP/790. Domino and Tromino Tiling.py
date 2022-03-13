class Solution:  # TLE
    def numTilings(self, n: int) -> int:
        memo = {}
        return self.dfs(n, 0, 0, memo)

    def dfs(self, n, r1, r2, memo):
        if (r1, r2) in memo:
            return memo[(r1, r2)]

        if r1 > n or r2 > n:
            return 0
        if r1 == n and r2 == n:
            return 1

        res = 0
        Domino1 = self.dfs(n, r1 + 2, r2 + 2, memo)  # 横着放 两个
        Domino2 = self.dfs(n, r1 + 1, r2 + 1, memo)
        Domino3 = self.dfs(n, r1 + 2, r2, memo)
        Domino4 = self.dfs(n, r1, r2 + 2, memo)

        Tromino1 = self.dfs(n, r1 + 2, r2 + 1, memo)
        Tromino2 = self.dfs(n, r1 + 1, r2 + 2, memo)

        if r1 == r2:
            res += Domino1 + Domino2 + Tromino1 + Tromino2
        if r1 - r2 == 1:
            res += Domino4 + Tromino2
        if r2 - r1 == 1:
            res += Domino3 + Tromino1

        memo[(r1, r2)] = res % (10 ** 9 + 7)
        return memo[(r1, r2)]


class Solution1:
    def numTilings(self, n: int) -> int:
        memo = {}

        return self.dp(n, 0, 0, memo) % (10 ** 9 + 7)

    def dp(self, n, row1, row2, memo):  # 2D state: for each row how many squares we filled in from left to tight
        if (row1, row2) in memo:
            return memo[(row1, row2)]

        if row1 > n or row2 > n:
            return 0

        res = 0

        if row1 == n and row2 == n:
            return 1
        if row1 == row2:
            res += self.dp(n, row1 + 1, row2 + 1, memo) + self.dp(n, row1 + 2, row2 + 2, memo) + self.dp(n, row1 + 2,
                                                                                                         row2 + 1,
                                                                                                         memo) + self.dp(
                n, row1 + 1, row2 + 2, memo)
        if row1 == row2 + 1:
            res += self.dp(n, row1, row2 + 2, memo) + self.dp(n, row1 + 1, row2 + 2, memo)
        if row2 == row1 + 1:
            res += self.dp(n, row1 + 2, row2, memo) + self.dp(n, row1 + 2, row2 + 1, memo)

        memo[(row1, row2)] = res
        return memo[(row1, row2)]
