class Solution:
    def validPalindrome(self, s: str) -> bool:

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return self.isValid(s, left + 1, right) or self.isValid(s, left, right - 1)

        return True

    def isValid(self, s, left, right):
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True