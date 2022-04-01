class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # start from gates ---> better than start from empty room

        queue = collections.deque()
        visited = set()
        m, n = len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:  # gates
                    queue.append((0, i, j))  # initialization
                    visited.add((i, j))

        while queue:
            dist, i, j = queue.popleft()
            if dist < rooms[i][j]:
                rooms[i][j] = dist

            for dx, dy in (1, 0), (0, 1), (0, -1), (-1, 0):
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and rooms[x][y] != -1 and (x, y) not in visited:
                    queue.append((dist + 1, x, y))
                    visited.add((x, y))

        return rooms