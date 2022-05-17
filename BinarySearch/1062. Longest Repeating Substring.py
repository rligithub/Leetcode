class Solution1:
    def longestRepeatingSubstring(self, s: str) -> int:
        # copy book --> binary search length of substring --> check if it's repeating
        # 注意 ababa结果为3个，因为aba 可以重复

        n = len(s)

        left, right = 1, n

        while left <= right:  # find right boundary
            mid = left + (right - left) // 2
            if self.isRepeated(s, mid):
                left = mid + 1
            else:
                right = mid - 1

        return left - 1

    def isRepeated(self, s, size):

        seen = set()

        for i in range(len(s) - size + 1):
            substr = s[i:i + size]
            if substr in seen:
                return True
            seen.add(substr)

        return False


class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        # copy book --> binary search length of substring --> check if it's repeating
        # 注意 ababa结果为3个，因为aba 可以重复

        n = len(s)

        left, right = 0, n - 1
        while left < right:
            mid = left + (right - left + 1) // 2  # difference

            if self.isRepeated(s, mid):
                left = mid
            else:
                right = mid - 1
        return left

    def isRepeated(self, s, size):

        seen = set()

        for i in range(len(s) - size + 1):
            substr = s[i:i + size]
            if substr in seen:
                return True
            seen.add(substr)

        return False
