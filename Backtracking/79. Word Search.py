class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 给一个board，问这个单词在不在里面

        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.dfs(board, word, m, n, 0, i, j, set()):
                        return True
        return False

    def dfs(self, board, word, m, n, pos, i, j, visited):
        if pos == len(word):
            return True

        if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited or board[i][j] != word[pos]:
            return False

        visited.add((i, j))

        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            x = i + dx
            y = j + dy

            if self.dfs(board, word, m, n, pos + 1, x, y, visited):
                return True
        visited.remove((i, j))  # backtrack --> remove incorrect path
        return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 给一个board，问这个单词在不在里面

        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):

                if self.dfs(board, word, m, n, 0, i, j, set()):
                    return True
        return False

    def dfs(self, board, word, m, n, pos, i, j, visited):
        if pos == len(word):
            return True

        if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited or board[i][j] != word[pos]:
            return False

        visited.add((i, j))

        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            x = i + dx
            y = j + dy

            if self.dfs(board, word, m, n, pos + 1, x, y, visited):
                return True
        visited.remove((i, j))  # backtrack --> remove incorrect path
        return False