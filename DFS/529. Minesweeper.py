class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        m, n = len(board), len(board[0])
        visited = set()
        i, j = click[0], click[1]
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        elif board[i][j] == 'E':
            self.dfs(directions, board, m, n, i, j, visited)
            return board

    def dfs(self, directions, board, m, n, i, j, visited):
        visited.add((i, j))

        M_cnt = 0
        for dx, dy in directions:
            x, y = i + dx, j + dy
            if 0 <= x < m and 0 <= y < n and board[x][y] == 'M':
                M_cnt += 1
        if M_cnt == 0:
            board[i][j] = 'B'
        else:
            board[i][j] = str(M_cnt)
            return

        for dx, dy in directions:
            x, y = i + dx, j + dy
            if 0 <= x < m and 0 <= y < n and (x, y) not in visited and board[x][y] == 'E':
                self.dfs(directions, board, m, n, x, y, visited)

