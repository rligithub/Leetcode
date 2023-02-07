class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        # remove interval ---> similar to insert interval

        res = []
        for start, end in intervals:
            if start >= toBeRemoved[1] or end <= toBeRemoved[0]:  # no overlapping
                res.append([start, end])
            else:
                if start < toBeRemoved[0]:
                    res.append([start, toBeRemoved[0]])
                if end > toBeRemoved[1]:
                    res.append([toBeRemoved[1], end])

        return res