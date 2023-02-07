class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        # simiar to 857. mini cost to hire k workers

        # min(efficiency) * sum of speed ---> sort by efficiency (large to smaller)
        # for loop, sumSpeed ++, pop min speed if over k, sumSpeed -- , get max res

        workers = []
        for i in range(n):
            workers.append((efficiency[i], speed[i]))

        workers.sort(key=lambda x: -x[0])

        mod = 10 ** 9 + 7
        res = 0
        heap = []
        sumSpeed = 0
        for efficiency, speed in workers:
            heapq.heappush(heap, speed)
            sumSpeed += speed

            if len(heap) > k:
                sumSpeed -= heapq.heappop(heap)

            if len(heap) <= k:  # 题目说最多k个，没说一定要选k个
                res = max(res, efficiency * sumSpeed)

        return res % mod
