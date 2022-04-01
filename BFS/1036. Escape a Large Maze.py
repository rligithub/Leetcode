class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if not blocked:
            return True

        n = len(blocked) * len(blocked) // 2
        blocks = set()
        for (x, y) in blocked:
            blocks.add((x, y))

        return self.bfs(blocks, n, source[0], source[1], target) & self.bfs(blocks, n, target[0], target[1], source)

    def bfs(self, blocks, n, i, j, target):
        queue = collections.deque()
        queue.append((i, j))
        visited = set()
        visited.add((i, j))

        while queue:
            i, j = queue.popleft()
            if [i, j] == target or len(visited) >= n:
                return True

            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                x = i + dx
                y = j + dy
                if 0 <= x < 10 ** 6 and 0 <= y < 10 ** 6 and (x, y) not in blocks and (x, y) not in visited:
                    queue.append((x, y))
                    visited.add((x, y))

        return False