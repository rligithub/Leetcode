"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = sorted([i for s in schedule for i in s], key=lambda x: x.start)
        res = []
        curEnd = intervals[0].end
        for interval in intervals[1:]:
            if curEnd < interval.start: # non overlapping
                res.append(Interval(curEnd, interval.start))
            curEnd = max(curEnd, interval.end)
        return res