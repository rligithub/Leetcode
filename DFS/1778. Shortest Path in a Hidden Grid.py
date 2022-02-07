# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
# class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#
#
#    def move(self, direction: str) -> bool:
#
#
#    def isTarget(self) -> None:
#
#

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:

        # step1: first use dfs to find all possible reachable positions
        opposite = {"U": "D", "D": "U", "L": "R", "R": "L"}

        # build graph --> store each position and if it is destination
        graph = {}
        graph[(0, 0)] = master.isTarget()

        self.dfs(master, opposite, graph, 0, 0)

        # step2: now use bfs to find the minimum distance
        queue = collections.deque([(0, 0, 0)])  # (r, c, dist)
        visited = set()

        while queue:
            i, j, dist = queue.popleft()
            if graph[(i, j)] == True:
                return dist

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x = i + dx
                y = j + dy
                if (x, y) in graph and (x, y) not in visited:
                    visited.add((x, y))
                    queue.append((x, y, dist + 1))

        return -1

    def dfs(self, master, opposite, graph, i, j):
        for dire, dx, dy in ("U", -1, 0), ("D", 1, 0), ("L", 0, -1), ("R", 0, 1):
            x = i + dx
            y = j + dy
            if (x, y) not in graph and master.canMove(dire):
                # move forward
                master.move(dire)
                graph[(x, y)] = master.isTarget()
                self.dfs(master, opposite, graph, x, y)
                # move back
                master.move(opposite[dire])