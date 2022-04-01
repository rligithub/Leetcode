class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        # BFS + heap(initialization(cut shortest tree first) )

        # step1: push all trees in heap
        m, n = len(forest), len(forest[0])
        heap = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    heapq.heappush(heap, ((forest[i][j], i, j)))

        # step2: pop heap (with shortest tree priority) --> do bfs check the distance between start position and this tree position
        dist = 0
        start = [0, 0]
        while heap:
            height, i, j = heapq.heappop(heap)
            step = self.bfs(forest, m, n, start, [i, j])

            if step == -1:
                return -1
            dist += step
            start = [i, j]  # new_start positions ---> current position

        return dist

    def bfs(self, forest, m, n, start, destination):

        queue = collections.deque()
        queue.append((start[0], start[1], 0))
        visited = set()
        visited.add((start[0], start[1]))

        while queue:
            i, j, step = queue.popleft()
            if [i, j] == destination:
                return step

            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited and forest[x][y] != 0:
                    queue.append((x, y, step + 1))
                    visited.add((x, y))

        return -1