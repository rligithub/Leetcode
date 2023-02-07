class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        # hashmap = {room: endTime1, endTime2, endTime3}
        # heap --> (hashmap[room][-1], room) ==> pop early endTime
        # append ===> hashmap[room].append(hashmap[room][-1] + duration)

        hashmap = collections.defaultdict(list)
        heap = []
        for i in range(n):
            heapq.heappush(heap, (0, i))  # (endTime, roomID)
            hashmap[i].append(0)

        meetings.sort()  # sort based on start time

        for start, end in meetings:
            duration = end - start

            while heap[0][
                0] < start:  # update last end time --> make sure pop min room_id for all available room(set same end time)
                curTime, rm = heapq.heappop(heap)
                heapq.heappush(heap, (start, rm))

            curTime, rm = heapq.heappop(heap)
            heapq.heappush(heap, (max(curTime, start) + duration, rm))
            hashmap[rm].append(max(curTime, start) + duration)

        maxx = 0
        res = 0
        for rm in hashmap.keys():
            if maxx < len(hashmap[rm]):
                maxx = len(hashmap[rm])
                res = rm
        return res

