class Solution1:
    def isPalindrome(self, s: str) -> bool:
        # 移除all non-alphanumeric characters
        left, right = 0, len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False

        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 移除all non-alphanumeric characters
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False

        return True 