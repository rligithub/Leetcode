class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # 把intervals按start从小到大排列，然后按end从大到小排列 --> 看是否有cover后面的intervals
        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        curEnd = 0
        for start, end in intervals:

            if curEnd < end:
                curEnd = end
                count += 1  # non-overlapping intervals

            # curEnd >= end: covered the intervals, do not do anything
        return count

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x : (x[0], -x[1]))

        res = []
        res.append(intervals[0])
        for i, j in intervals[1:]:
            if res[-1][1] >= j: # known that i < res[-1][0] for sure, now j < res[-1][1] --> fully covered
                continue
            else:
                res.append([i, j])
        return len(res)