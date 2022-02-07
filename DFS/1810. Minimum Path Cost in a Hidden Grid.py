# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
# class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#
#
#    def move(self, direction: str) -> int:
#
#
#    def isTarget(self) -> None:
#
#

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        directions = ("U", -1, 0), ("D", 1, 0), ("L", 0, -1), ("R", 0, 1)
        opposite = {"U": "D", "D": "U", "L": "R", "R": "L"}

        # step1 --> dfs to record all reachable locations with cost
        # build graph
        graph = {}
        graph[(0, 0)] = master.isTarget()
        destination = [None, None]
        self.dfs(master, directions, opposite, destination, 0, 0, graph)

        # step2 --> priority queue(heap) to find min cost
        heap = []
        heap.append((0, 0, 0))  # i, j, cost
        visited = set()
        visited.add((0, 0))

        while heap:
            cost, i, j = heapq.heappop(heap)
            if (i, j) == (destination[0], destination[1]):  # if is target
                return cost

            for d, dx, dy in directions:
                x = i + dx
                y = j + dy
                if (x, y) in graph and (x, y) not in visited:
                    visited.add((x, y))
                    heapq.heappush(heap, (cost + graph[(x, y)], x, y))

        return -1

    def dfs(self, master, directions, opposite, destination, i, j, graph):
        if master.isTarget():
            destination[0], destination[1] = i, j
        for d, dx, dy in directions:
            x = i + dx
            y = j + dy
            if (x, y) not in graph and master.canMove(d):
                graph[(x, y)] = master.move(d)
                self.dfs(master, directions, opposite, destination, x, y, graph)
                master.move(opposite[d])







