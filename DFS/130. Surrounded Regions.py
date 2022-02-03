class Solution:  # in-place modify --> DFS
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # step1 --> for loop each "O" in 最外围 --> do dfs
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    self.dfs(board, i, j, m, n)

        # step2 --> for loop each points to modify
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'v':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

    def dfs(self, board, i, j, m, n):
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
            return

        board[i][j] = 'v'

        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            self.dfs(board, i + dx, j + dy, m, n)