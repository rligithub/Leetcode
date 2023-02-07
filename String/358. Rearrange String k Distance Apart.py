class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        # similar to #767, but pop k char each time

        if not s:
            return ""
        if k == 0:
            return s
        freq = collections.Counter(s)
        heap = [[-count, char] for char, count in freq.items()]
        heapq.heapify(heap)
        res = ""

        while len(heap) >= k:
            temp = []
            for _ in range(k):
                count, char = heapq.heappop(heap)
                temp.append((count, char))
                res += char
            for count, char in temp:
                if count < -1:
                    heapq.heappush(heap, [count + 1, char])

        if len(heap) == 0:
            return res
        else:
            while heap:
                count, char = heapq.heappop(heap)
                if count < -1:
                    return ""
                else:
                    res += char
            return res

