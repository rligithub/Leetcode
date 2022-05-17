class Solution:
    def longestDupSubstring(self, s: str) -> str:
        # similar to #1062 - longest repeating substring --> get size of substring
        # this question requires to print out substring

        # binary search num of size --> check if it's valid

        res = ''
        left, right = 0, len(s)
        while left <= right:
            mid = left + (right - left) // 2

            substr = self.isRepeated(s, mid)
            if substr:
                res = substr
                left = mid + 1
            else:
                right = mid - 1

        return res

    def isRepeated(self, s, size):

        seen = set()

        for i in range(len(s) - size + 1):
            substr = s[i:i + size]
            if substr in seen:
                return substr
            seen.add(substr)
        return ''

class Solution:
    def longestDupSubstring(self, s: str) -> str:

        start = 0
        left, right = 1, len(s)

        while left <= right:
            mid = left + (right - left) // 2
            pos = self.isRepeated(s, mid)
            if pos != -1:
                start = pos
                left = mid + 1
            else:
                right = mid - 1

        return s[start:start + left - 1]

    def isRepeated(self, s, size):

        seen = set()
        for i in range(len(s) - size + 1):
            substr = s[i:i + size]
            if substr in seen:
                return i
            seen.add(substr)
        return -1



