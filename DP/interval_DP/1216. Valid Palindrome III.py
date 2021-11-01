class Solution1:  # top down dp 双序列
    def isValidPalindrome(self, s: str, k: int) -> bool:
        # 一个string最多 移除k位，求能否得到一个 palindrome
        # palindrome -- > reverse string[::-1]
        # LCS -- > min steps
        # k--> max steps

        memo = {}

        LCS = self.dfs(s, s[::-1], 0, 0, memo)

        return len(s) - LCS <= k

    def dfs(self, s, r, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        n = len(s)
        if i > n - 1 or j > n - 1:
            return 0

        if s[i] == r[j]:
            res = self.dfs(s, r, i + 1, j + 1, memo) + 1
        else:
            res = max(self.dfs(s, r, i + 1, j, memo), self.dfs(s, r, i, j + 1, memo))

        memo[(i, j)] = res

        return memo[(i, j)]


class Solution:  # top down dp 区间
    def isValidPalindrome(self, s: str, k: int) -> bool:
        # 一个string最多 移除k位，求能否得到一个 palindrome
        # LCS -- > min steps
        # k--> max steps

        memo = {}

        return len(s) - self.dfs(s, 0, len(s) - 1, memo) <= k

    def dfs(self, s, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == j:
            return 1
        if i > j:
            return 0

        if s[i] == s[j]:
            res = self.dfs(s, i + 1, j - 1, memo) + 2
        else:
            res = max(self.dfs(s, i + 1, j, memo), self.dfs(s, i, j - 1, memo))

        memo[(i, j)] = res
        return memo[(i, j)]