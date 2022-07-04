class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # x1 x2  ---> y1 y2
        # x1 x2 ---> y2 y1
        # two cases --> first part of s1 match to frst part of s2/ first part of s1 match to second part of s2
        if len(s1) != len(s2):
            return False
        memo = {}
        return self.dfs(s1, s2, memo)

    def dfs(self, s1, s2, memo):
        if (s1, s2) in memo:
            return memo[(s1, s2)]

        if s1 == s2:
            return True

        if sorted(s1) != sorted(s2):
            return False

        for i in range(1, len(s1)):
            if (self.dfs(s1[:i], s2[:i], memo) and self.dfs(s1[i:], s2[i:], memo)) or (
                    self.dfs(s1[i:], s2[:-i], memo) and self.dfs(s1[:i], s2[-i:], memo)):
                memo[(s1, s2)] = True
                return True
        memo[(s1, s2)] = False
        return False

