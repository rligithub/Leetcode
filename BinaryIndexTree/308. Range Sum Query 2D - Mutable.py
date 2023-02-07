class BinaryIndexTree:
    def __init__(self, m, n):
        self.summ = [[0] * (n + 1) for _ in range(m + 1)]

    def _lowbit(self, x):
        return x & (-x)

    def update(self, row, col, delta):
        m, n = len(self.summ), len(self.summ[0])
        i = row
        while i < m:
            j = col
            while j < n:
                self.summ[i][j] += delta
                j += self._lowbit(j)
            i += self._lowbit(i)

    def query(self, row, col):
        res = 0
        i = row
        while i > 0:
            j = col
            while j > 0:
                res += self.summ[i][j]
                j -= self._lowbit(j)
            i -= self._lowbit(i)
        return res


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.matrix = matrix
        self.tree = BinaryIndexTree(m, n)
        for i in range(m):  # build tree
            for j in range(n):
                self.tree.update(i + 1, j + 1, matrix[i][j])

    def update(self, row: int, col: int, val: int) -> None:
        self.tree.update(row + 1, col + 1, val - self.matrix[row][col])  # update prefsumm in tree
        self.matrix[row][col] = val  # update nums

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.tree.query(row2 + 1, col2 + 1) - self.tree.query(row2 + 1, col1) - self.tree.query(row1,
                                                                                                       col2 + 1) + self.tree.query(
            row1, col1)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)