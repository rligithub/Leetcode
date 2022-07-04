# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

from sortedcontainers import SortedList
from sortedcontainers import SortedDict
import collections

class MyCalendar1:  # 暴力法

    def __init__(self):
        self.calender = []

    def book(self, start: int, end: int) -> bool:
        for event in self.calender:
            if event[0] < end and event[1] > start:  # double booking
                return False

        self.calender.append([start, end])
        return True


class MyCalendar2:
    def __init__(self):
        self.calender = SortedList()

    def book(self, start: int, end: int) -> bool:
        pos = self.calender.bisect_right(start)

        if pos == len(self.calender) or pos % 2 == 0 and self.calender[pos] >= end:
            self.calender.add(start)
            self.calender.add(end)
            return True
        return False


class MyCalendar:
    def __init__(self):
        self.calender = SortedDict()

    def book(self, start: int, end: int) -> bool:
        idx = self.calender.bisect_right(start)
        if 0 <= idx < len(self.calender):
            if self.calender.values()[idx] < end:
                return False
        self.calender[end] = start
        print(self.calender, idx, start)
        return True
