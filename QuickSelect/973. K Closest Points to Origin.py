class SolutionTLE:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # quick sort --> small to large
        return self.quickSelect(points, 0, len(points) - 1, k)

    def quickSelect(self, points, left, right, k):
        pivot = self.partition(points, left, right)
        if pivot == k - 1:
            return points[:pivot + 1]
        elif pivot > k - 1:
            return self.quickSelect(points, left, pivot - 1, k)
        else:
            return self.quickSelect(points, pivot + 1, right, k)

    def partition(self, points, left, right):
        if left == right:
            return left
        pivot = random.randint(left, right)

        points[pivot], points[right] = points[right], points[pivot]

        targetDist = points[right][1] ** 2 + points[right][0] ** 2

        slow = left
        for fast in range(left, right):
            dist = points[fast][1] ** 2 + points[fast][0] ** 2
            if dist < targetDist:
                points[slow], points[fast] = points[fast], points[slow]
                slow += 1

        points[slow], points[right] = points[right], points[slow]
        return slow


class Solution2:
    def kClosest(self, points, K):
        points.sort(key=lambda P: P[0] ** 2 + P[1] ** 2)
        return points[:K]


class Solution:
    def kClosest(self, points, k: int):
        # Since heap is sorted in increasing order,
        # negate the distance to simulate max heap
        # and fill the heap with the first k elements of points
        heap = [(-self.squared_distance(points[i]), i) for i in range(k)]
        heapq.heapify(heap)
        for i in range(k, len(points)):
            dist = -self.squared_distance(points[i])
            if dist > heap[0][0]:
                # If this point is closer than the kth farthest,
                # discard the farthest point and add this one
                heapq.heappushpop(heap, (dist, i))

        # Return all points stored in the max heap
        return [points[i] for (_, i) in heap]

    def squared_distance(self, point) -> int:
        """Calculate and return the squared Euclidean distance."""
        return point[0] ** 2 + point[1] ** 2


import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        heap = []

        for (x, y) in points:
            dist = -(x * x + y * y)
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))

        return [(x, y) for (dist, x, y) in heap]