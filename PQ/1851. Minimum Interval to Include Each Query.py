class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # similar to # 1353 max number of events that can be attended
        n = len(intervals)

        qr = []
        for i, q in enumerate(queries):
            qr.append((q, i))
        qr.sort()  # sort by query value

        intervals.sort()

        heap = []
        cur = 0
        res = [-1] * len(queries)

        for q, i in qr:

            while cur < n and q >= intervals[cur][0]:  # 如果q 大于 interval start的值， heap里放（size，end）
                size = intervals[cur][1] - intervals[cur][0] + 1
                heapq.heappush(heap, (size, intervals[cur][1]))
                cur += 1

            while heap and q > heap[0][1]:  # 不符合的，如果当前q 超过intevral end的都pop掉
                heapq.heappop(heap)

            if heap:  # 只peak，size最小的符合条件
                size, end = heap[0]
                res[i] = size

        return res