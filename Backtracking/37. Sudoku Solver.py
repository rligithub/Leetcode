class Solution1:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] != '.':
                    continue
                for k in range(1, 10):
                    if self.isValid(board, i, j, str(k)) and self.solveSudoku(board):
                        return True
                    board[i][j] = '.'
                return False
        return True

    def isValid(self, board, i, j, k):
        for x in range(len(board)):
            if board[x][j] == k:
                return False

        for y in range(len(board[0])):
            if board[i][y] == k:
                return False

        for x in range(3):
            for y in range(3):
                if board[(i // 3) * 3 + x][(j // 3) * 3 + y] == k:
                    return False
        board[i][j] = k
        return True

