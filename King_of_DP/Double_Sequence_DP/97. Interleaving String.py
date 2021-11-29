class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # i, j, i + j --> index of s1, index of s2, index of s3
        if len(s1) + len(s2) != len(s3):
            return False
        memo = {}
        return self.dfs(s1, s2, s3, 0, 0, memo)

    def dfs(self, s1, s2, s3, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == len(s1) and j == len(s2):
            return True

            # CASE1 s1 == s3
        if i < len(s1) and s1[i] == s3[i + j] and self.dfs(s1, s2, s3, i + 1, j, memo):
            memo[(i, j)] = True
            return True

            # CASE2 s2 == s3
        if j < len(s2) and s2[j] == s3[i + j] and self.dfs(s1, s2, s3, i, j + 1, memo):
            memo[(i, j)] = True
            return True

        memo[(i, j)] = False
        return False
