class Solution:  # top down dp
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

        if i < n and j < n and s[i] == r[j]:
            res = self.dfs(s, r, i + 1, j + 1, memo) + 1
        else:
            res = max(self.dfs(s, r, i + 1, j, memo), self.dfs(s, r, i, j + 1, memo))

        memo[(i, j)] = res

        return memo[(i, j)]