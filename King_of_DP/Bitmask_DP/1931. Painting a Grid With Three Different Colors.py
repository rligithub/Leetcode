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

class Solution: # happiness method
    def colorTheGrid(self, m: int, n: int) -> int:
        memo = {}
        return self.dfs(m, n, 0, 0, 0, 0, memo)

    def dfs(self, m, n, pos, red, yellow, green, memo):
        if (pos, red, yellow, green) in memo:
            return memo[(pos, red, yellow, green)]

        if pos == n*m:
            return 1

        row, col = pos // m, pos % m

        mod = 10 ** 9 + 7
        fullmask = (1 << m) - 1

        nxt_red = (red << 1) & fullmask
        nxt_yellow = (yellow << 1) & fullmask
        nxt_green = (green << 1) & fullmask

        res = 0
        if self.valid(m, row, col, red):
            res += self.dfs(m, n, pos + 1, nxt_red + 1, nxt_yellow, nxt_green, memo)
        if self.valid(m, row, col, yellow):
            res += self.dfs(m, n, pos + 1, nxt_red, nxt_yellow + 1, nxt_green, memo)
        if self.valid(m, row, col, green):
            res += self.dfs(m, n, pos + 1, nxt_red, nxt_yellow, nxt_green + 1, memo)

        memo[(pos, red, yellow, green)] = res % mod
        return memo[(pos, red, yellow, green)]

    def valid(self, m, row, col, state):
        up = 1 << (m - 1)

        if col == 0 and row == 0:
            return True

        if col > 0 and state & 1:  # has neighbor
            return False

        if row > 0 and state & up:  # has neighbor
            return False

        return True

