class Solution:
    def longestPalindrome(self, s: str) -> int:
        # 找出由这些 char组成的最长palindrome的个数

        counter = collections.Counter(s)

        res = 0

        for cnt in counter.values():
            res += cnt // 2 * 2
            if res % 2 == 0 and cnt % 2 == 1:
                res += 1
        return res