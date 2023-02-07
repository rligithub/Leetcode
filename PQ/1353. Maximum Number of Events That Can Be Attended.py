class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # similr to course schedule III

        # sort by events startTime
        # 枚举每一时刻的状态，判断是否可以参加会议 ---> 删掉过期会议,  加入可选会议,  参加最早结束的会议

        events.sort()

        heap = []
        i = 0
        count = 0
        min_day = events[0][0]
        max_day = max(x[1] for x in events)

        for cur in range(min_day, max_day + 1):
            # add events priortized by earliest end date
            while i < len(events) and cur >= events[i][0]:
                heapq.heappush(heap, events[i][1])
                i += 1

            # discard past events since we can't attend them anymore.
            while heap and cur > heap[0]:
                heapq.heappop(heap)

            # attend an event with earliest end date
            if heap:
                heapq.heappop(heap)
                count += 1

        return count