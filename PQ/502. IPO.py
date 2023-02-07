class Solution1:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = []
        for i in range(n):
            projects.append((capital[i], profits[i]))
        projects.sort(key=lambda x: x[0])

        heap = []
        i = 0
        for _ in range(k):
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(heap, -projects[i][1])  # push add small capital's profits into heap
                i += 1
            if heap:
                w -= heapq.heappop(heap)  # pop k times from heap --> original capital += profit

        return w

