class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # 找有几块 大片X -- > similar to # of islands

        m, n = len(board), len(board[0])

        count = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    if (i, j) not in visited:
                        self.dfs(board, i, j, visited)
                        count += 1
        return count

    def dfs(self, board, i, j, visited):
        visited.add((i, j))
        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            x = i + dx
            y = j + dy
            if 0 <= x < len(board) and 0 <= y < len(board[0]) and (x, y) not in visited and board[x][y] == 'X':
                self.dfs(board, x, y, visited)

