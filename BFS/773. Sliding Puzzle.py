class Solution:
    def slidingPuzzle(self, board) -> int:
        # 拉直了
        initial = ''
        for i in range(len(board)):
            for j in range(len(board[0])):
                initial += str(board[i][j])

        if initial == "123450":
            return 0

        queue = collections.deque()
        queue.append((initial, 0))
        visited = set()
        visited.add((initial))

        while queue:
            status, step = queue.popleft()
            if status == '123450':
                return step

            for next_status in self.getNxt(status):
                if next_status not in visited:
                    queue.append((next_status, step + 1))
                    visited.add(next_status)

        return -1

    def getNxt(self, status):
        graph = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]

        res = []
        s = list(status)
        pos = s.index("0")
        for swap_pos in graph[pos]:
            s[pos], s[swap_pos] = s[swap_pos], s[pos]
            res.append("".join(s))
            s[pos], s[swap_pos] = s[swap_pos], s[pos]  # backtrack
        return res



