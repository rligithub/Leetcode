class Solution1:  # 先放 再检查valid
    def solveNQueens(self, n: int) -> List[List[str]]:

        # use arr to save Q's position --> idex stands for row and value stands for col
        res = []
        path = []
        Q = [-1] * n  # Q[row] = col
        self.dfs(n, Q, 0, path, res)
        return res

    def dfs(self, n, Q, pos, path, res):

        if pos == n:
            res.append(path)
            return

        for col in range(n):  # Q[row] = col
            Q[pos] = col  # 第几行 记录一下第几列  放了Q
            if self.isValid(n, Q, pos):  # check if cur row is valid
                s = '.' * n
                self.dfs(n, Q, pos + 1, path + [s[:col] + 'Q' + s[col + 1:]], res)

    def isValid(self, n, Q, row):
        for i in range(row):
            # same column or abs(col_i - cur_col) == abs(row_i - cur_row)
            if Q[i] == Q[row] or abs(Q[i] - Q[row]) == abs(i - row):
                return False
        return True


class Solution:  # same solution -> 先检查 valid 再放
    def solveNQueens(self, n: int) -> List[List[str]]:

        # use arr to save Q's position --> idex stands for row and value stands for col
        res = []
        path = []
        Q = [-1] * n  # Q[row] = col
        self.dfs(n, Q, 0, path, res)
        return res

    def dfs(self, n, Q, pos, path, res):

        if pos == n:
            res.append(path)
            return

        for col in range(n):  # Q[row] = col

            if self.isValid(n, Q, pos, col):  # check if cur row is valid
                s = '.' * n
                self.dfs(n, Q, pos + 1, path + [s[:col] + 'Q' + s[col + 1:]], res)

    def isValid(self, n, Q, cur_row, cur_col):
        for i in range(cur_row):
            if Q[i] == cur_col or abs(Q[i] - cur_col) == abs(i - cur_row):
                return False
        Q[cur_row] = cur_col
        return True





