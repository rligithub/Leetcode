class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        directions = [[2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2]]
        queue = collections.deque()
        queue.append((0, 0, 0))
        visited = set()
        visited.add((0, 0))

        while queue:
            i, j, step = queue.popleft()
            if i == abs(x) and j == abs(y):
                return step

            for dx, dy in directions:
                ii = i + dx
                jj = j + dy
                if ii >= -2 and jj >= -2 and (ii, jj) not in visited:
                    queue.append((ii, jj, step + 1))
                    visited.add((ii, jj))

