class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # wage = ratio * Sum of quality 先确定ratio --->  性价比从低到高排列，但是价钱由性价比低的那个人决定
        # for loop每个ratio，Sum of quality ++, 如果超过k个人，则pop掉 高 quality的人，Sum of quality --, 使得wage minimumize

        n = len(quality)
        workers = []
        for i in range(n):
            ratio = wage[i] / quality[i]
            workers.append((ratio, quality[i], wage[i]))

        workers.sort()

        res = float('inf')
        heap = []
        sumq = 0
        for ratio, q, w in workers:
            heapq.heappush(heap, -q)
            sumq += q  # 先把性价比低的quality加入

            if len(heap) > k:  # 踢掉 大quality 的， 因为 minWage = ratio * quality
                sumq += heapq.heappop(heap)

            if len(heap) == k:
                res = min(res, ratio * sumq)

        return float(res)
