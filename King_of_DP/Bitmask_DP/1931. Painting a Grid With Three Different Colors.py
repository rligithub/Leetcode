class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        # maintain a silding window size m
        # check above neighbor --> prev_row[j]
        # check left neighbor --> prev_row[j-1] (value has been updated)
        '''
        0 234
        5 6  --> cur value is 6, prev_row[j] = 2, prev_row[j-1] = 0 but it was replaced by 5.
        '''

        memo = {}
        return self.dfs(m, n, 0, tuple([0] * m), memo)

    def dfs(self, m, n, pos, prevrow, memo):
        if (pos, prevrow) in memo:
            return memo[(pos, prevrow)]

        if pos == m * n:
            return 1

        mod = 10 ** 9 + 7

        row = pos // m
        col = pos % m

        prevrowlist = list(prevrow)
        res = 0

        neighborColors = set()
        if row > 0:
            neighborColors.add(prevrowlist[col])  # check above nrighbor

        if col > 0:
            neighborColors.add(prevrowlist[col - 1])  # check left nrighbor

        for c in (0, 1, 2):
            if c not in neighborColors:
                newprevrow = prevrowlist
                newprevrow[col] = c
                res += self.dfs(m, n, pos + 1, tuple(newprevrow), memo)

        memo[(pos, prevrow)] = res % mod
        return memo[(pos, prevrow)]
