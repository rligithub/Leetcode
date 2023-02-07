class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])

        count = 0
        curEnd = float('-inf')
        for start, end in intervals:
            print(start, end, curEnd)
            if curEnd <= start:
                curEnd = end
            else:
                count += 1

        return count

