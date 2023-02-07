class Solution:  # binary search + rolling hash
    def longestDupSubstring(self, s: str) -> str:
        # binary search for size to see if it is repeated
        start = 0
        left, right = 1, len(s) - 1

        while left <= right:
            mid = left + (right - left) // 2
            pos = self.isRepeated(s, mid)
            if pos != -1:  # find right boundary
                start = pos
                left = mid + 1
            else:
                right = mid - 1

        return s[start: start + left - 1]

    def isRepeated(self, s, k):
        mod = 2 ** 64 - 1
        hashcode = 0
        base = 26

        for i in range(k):
            rightnum = ord(s[i]) - ord("a")
            hashcode = (hashcode * base + rightnum) % mod

        power = pow(base, k, mod)
        seen = {hashcode}
        for i in range(k, len(s)):
            rightnum = ord(s[i]) - ord("a")
            leftnum = ord(s[i - k]) - ord("a")
            hashcode = (hashcode * base + rightnum - power * leftnum) % mod
            if hashcode in seen:
                return i - k + 1
            else:
                seen.add(hashcode)

        return -1
