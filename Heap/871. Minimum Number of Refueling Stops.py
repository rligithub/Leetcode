class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        heap = []
        res = 0
        i = 0
        while startFuel < target:
            # heap is a priority queue that we store all available gas
            # distance <= 我的fuel就能到
            while i < len(stations) and stations[i][0] <= startFuel:
                heapq.heappush(heap, -stations[i][1])
                i += 1
            if not heap:
                return -1
            startFuel += -heapq.heappop(heap)
            res += 1
        return res