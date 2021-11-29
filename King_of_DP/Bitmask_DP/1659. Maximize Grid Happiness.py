class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        # 背包dp + bitmask -->需要知道intro当前个数 和 intro的state，extro当前个数和 extro的state
        # for loop当前的pos，维持一个n长度的intro state和extro state--> 来比较上一行邻居（state & (1 << (n-1))) 和左边的邻居 (state & 1)
        # intro的cost遇到邻居 - 30，由于每次pos从左往右移动，只需要比较上面和左边

        memo = {}
        return self.dfs(m, n, 0, introvertsCount, extrovertsCount, 0, 0, memo)

    def dfs(self, m, n, pos, inCount, exCount, inState, exState, memo):
        if (pos, inCount, exCount, inState, exState) in memo:
            return memo[(pos, inCount, exCount, inState, exState)]
        row, col = pos // n, pos % n

        if row == m:
            return 0
        fullmask = (1 << n) - 1

        nxt_inState = (inState << 1) & fullmask
        nxt_exState = (exState << 1) & fullmask

        res = self.dfs(m, n, pos + 1, inCount, exCount, nxt_inState, nxt_exState, memo)

        if inCount > 0:
            res = max(res,
                      self.dfs(m, n, pos + 1, inCount - 1, exCount, nxt_inState + 1, nxt_exState, memo) + self.cost(n,
                                                                                                                    row,
                                                                                                                    col,
                                                                                                                    inState,
                                                                                                                    exState,
                                                                                                                    -30) + 120)

        if exCount > 0:
            res = max(res,
                      self.dfs(m, n, pos + 1, inCount, exCount - 1, nxt_inState, nxt_exState + 1, memo) + self.cost(n,
                                                                                                                    row,
                                                                                                                    col,
                                                                                                                    inState,
                                                                                                                    exState,
                                                                                                                    +20) + 40)

        memo[(pos, inCount, exCount, inState, exState)] = res
        return memo[(pos, inCount, exCount, inState, exState)]

    def cost(self, n, row, col, inState, exState, val):
        res = 0
        up = 1 << (n - 1)
        if col > 0 and inState & 1:
            res += val - 30
        if row > 0 and inState & up:
            res += val - 30
        if col > 0 and exState & 1:
            res += val + 20
        if row > 0 and exState & up:
            res += val + 20

        return res

