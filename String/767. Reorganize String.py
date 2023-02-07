class Solution:
    def reorganizeString(self, s: str) -> str:
        if not s:
            return ""

        freq = collections.Counter(s)
        heap = [[-count, char] for char, count in freq.items()]
        heapq.heapify(heap)
        res = ""

        while len(heap) >= 2:
            count1, char1 = heapq.heappop(heap)  # pop most common char
            count2, char2 = heapq.heappop(heap)  # pop second most common char

            res += char1 + char2
            if count1 < -1:
                heapq.heappush(heap, [count1 + 1, char1])  # if count > 1, update count, add to heap for (-count, char)
            if count2 < -1:
                heapq.heappush(heap, [count2 + 1, char2])

        if len(heap) == 0:
            return res
        else:
            count, char = heapq.heappop(heap)
            if count < -1:  # if there is more than 2 counts for same char --> return ""
                return ""
            else:
                return res + char