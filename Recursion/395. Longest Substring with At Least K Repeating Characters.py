class Solution:  # recursion
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0

        counter = Counter(s)

        res = 0
        for i in range(len(s)):
            if counter[s[i]] < k:
                res = max(self.longestSubstring(s[:i], k), self.longestSubstring(s[i + 1:], k))
                break
            res += 1

        return res