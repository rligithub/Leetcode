class Solution:  # BFS
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # step1 --> for loop each "O" in 最外围 --> queue ---> bfs
        queue = collections.deque()
        visited = set()
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    if board[i][j] == 'O':
                        queue.append((i, j))
                        visited.add((i, j))

        while queue:
            i, j = queue.popleft()
            board[i][j] = 'v'

            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited and board[x][y] == 'O':
                    queue.append((x, y))
                    visited.add((x, y))

        # step2 --> for loop each points to modify
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'v':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'








