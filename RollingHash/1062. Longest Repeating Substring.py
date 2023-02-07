
class Solution:  # binary search + rolling hash
    def longestRepeatingSubstring(self, s: str) -> int:
        # similar to 1044. longest duplicate substring --> return subarray
        # binary search for size to see if it is repeated --> return size of subarray

        left, right = 0, len(s)

        while left <= right:
            mid = left + (right - left) // 2
            pos = self.isRepeated(s, mid)
            if pos != -1:
                left = mid + 1
            else:
                right = mid - 1
        return left - 1

    def isRepeated(self, s, k):
        n = len(s)
        base = 26
        hashcode = 0
        mod = 2** 63 - 1
        for i in range(k):
            rnum = ord(s[i]) - ord("a")
            hashcode = (hashcode * base + rnum) % mod

        seen = {hashcode}
        power = pow(base, k, mod)
        for i in range(k, n):
            lnum = ord(s[i - k]) - ord("a")
            rnum = ord(s[i]) - ord("a")
            hashcode = (hashcode * base + rnum - lnum * power) % mod
            if hashcode in seen:
                return i - k + 1
            else:
                seen.add(hashcode)

        return -1

