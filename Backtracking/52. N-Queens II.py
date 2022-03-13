class Solution1:  # use global res
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        Q = [-1] * n  # Q[row] = column
        self.dfs(n, Q, 0)
        return self.res

    def dfs(self, n, Q, pos):

        if pos == n:
            self.res += 1
            return

        for col in range(n):
            if self.isValid(n, Q, pos, col):
                self.dfs(n, Q, pos + 1)

    def isValid(self, n, Q, cur_row, cur_col):

        for i in range(cur_row):
            if Q[i] == cur_col or abs(Q[i] - cur_col) == abs(i - cur_row):
                return False

        Q[cur_row] = cur_col
        return True


class Solution:  # use local res --> return res
    def totalNQueens(self, n: int) -> int:
        res = 0
        Q = [-1] * n  # Q[row] = column
        return self.dfs(n, Q, 0)

    def dfs(self, n, Q, pos):

        if pos == n:
            return 1

        res = 0
        for col in range(n):
            if self.isValid(n, Q, pos, col):
                res += self.dfs(n, Q, pos + 1)
        return res

    def isValid(self, n, Q, cur_row, cur_col):

        for i in range(cur_row):
            if Q[i] == cur_col or abs(Q[i] - cur_col) == abs(i - cur_row):
                return False

        Q[cur_row] = cur_col
        return True
