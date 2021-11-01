class Solution:  # substring --> two pointer 中心开花（由中心散开）
    def longestPalindrome(self, s: str) -> str:

        res = ''
        for i in range(len(s)):
            res = max(self.twopointer(s, i, i), self.twopointer(s, i, i + 1), res, key=len)

        return res

    def twopointer(self, s, i, j):

        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1

        return s[i + 1:j]
