class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        res = []
        intervals.sort()
        res.append(intervals[0])
        for start, end in intervals[1:]:
            # if last meeting ends, then we start a new meeting
            if res[-1][1] < start:
                res.append([start, end])
            # if last meeting is going on, then we merge it by pick the latest finished time
            else:
                res[-1][1] = max(res[-1][1], end)
        return res
