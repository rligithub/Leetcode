class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # similar to 767

        if not tasks:
            return

        freq = collections.Counter(tasks)
        heap = [[-count, char] for char, count in freq.items()]
        heapq.heapify(heap)
        res = 0

        while heap:
            k = min(n + 1, len(heap))
            temp = []
            for _ in range(k):  # 在堆中取任务
                freq, char = heapq.heappop(heap)
                if freq != -1:
                    freq += 1
                    temp.append([freq, char])
            for node in temp:  # 将未执行完的任务放回堆中
                heapq.heappush(heap, node)
            if heap:  # 还有任务剩余
                res += n + 1  # 消耗的时间就是整个CD长度
            else:  # 所有任务完成了
                res += k  # 做了几个消耗就是几
        return res