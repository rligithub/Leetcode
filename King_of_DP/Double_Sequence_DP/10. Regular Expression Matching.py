class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        return self.dfs(s, p, 0, 0, memo)

    def dfs(self, s, p, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == len(s) and j == len(p):
            return True

        if j + 1 < len(p) and p[j + 1] == '*':
            # 如果*代表1个或者1个以上的前一个char，则必须要matched并且下一个比较要True 才行 --> s[i+1] vs. p[j]
            # 如果*代表0个前一个char，不用在乎p[j]是什么,直接比较下一个 --> s[i] vs. p[j+2]
            if self.matched(s, p, i, j) and self.dfs(s, p, i + 1, j, memo) or self.dfs(s, p, i, j + 2, memo):
                memo[(i, j)] = True
                return True
        if self.matched(s, p, i, j):
            if self.dfs(s, p, i + 1, j + 1, memo):
                memo[(i, j)] = True
                return True
        memo[(i, j)] = False
        return False

    def matched(self, s, p, i, j):
        if i == len(s) or j == len(p):
            return False
        return s[i] == p[j] or p[j] == '.'
