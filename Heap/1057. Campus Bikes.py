class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distances = []  # distances[worker] is tuple of (distance, worker, bike) for each bike
        for i, (x1, y1) in enumerate(workers):
            distances.append([])
            for j, (x2, y2) in enumerate(bikes):
                distance = abs(x1 - x2) + abs(y1 - y2)
                distances[-1].append((distance, i, j))
            distances[-1].sort(reverse=True)  # reverse so we can pop the smallest distance

        res = [None] * len(workers)
        used_bikes = set()
        dist = [distances[i].pop() for i in range(len(workers))]  # smallest distance for each worker
        heapq.heapify(dist)

        while len(used_bikes) < len(workers):
            _, worker, bike = heapq.heappop(dist)
            if bike not in used_bikes:
                res[worker] = bike
                used_bikes.add(bike)
            else:
                heapq.heappush(dist, distances[worker].pop())  # bike used, add next closest bike

        return res




           