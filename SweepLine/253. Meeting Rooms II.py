class Solution1:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # 找这些meeting有没有 重叠
        if not intervals:
            return 0

        start = []
        end = []
        for s, e in intervals:
            start.append(s)
            end.append(e)
        start.sort()
        end.sort()

        left, right = 0, 0
        res = 0

        # 找有几个meeting在当前结束时间 前 开始
        for i in range(len(start)):
            if start[i] < end[right]:
                res += 1
            else:
                right += 1
        return res


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # 数飞机

        meetings = []
        for start, end in intervals:
            meetings.append((start, 1))
            meetings.append((end, -1))

        meetings.sort()

        res = 0
        count = 0
        for time, meeting in meetings:
            count += meeting
            res = max(res, count)
        return res 