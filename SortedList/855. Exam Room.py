class ExamRoom  # TLE: # orderedSet ---> treeSet

    def __init__(self, n: int):
        self.n = n
        self.students = []

    def seat(self) -> int:
        if not self.students:
            student = 0
        else:
            dist, student = self.students[0], 0
            for i, s in enumerate(self.students):
                if i:
                    prev = self.students[i - 1]
                    d = (s - prev) // 2
                    if d > dist:
                        dist, student = d, prev + d

            d = self.n - 1 - self.students[-1]
            if d > dist:
                student = self.n - 1

        bisect.insort(self.students, student)
        return student

    def leave(self, p: int) -> None:
        self.students.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)

from sortedcontainers import SortedList


class ExamRoom  # TLE:

    def __init__(self, n: int):
        self.sl = SortedList()
        self.n = n

    def seat(self) -> int:
        if len(self.sl) == 0:
            pos = 0
        else:
            pos = 0
            maxi = self.sl[0] - 0
            for i in range(1, len(self.sl)):
                if (self.sl[i] - self.sl[i - 1]) // 2 > maxi:
                    pos = (self.sl[i] + self.sl[i - 1]) // 2
                    maxi = (self.sl[i] - self.sl[i - 1]) // 2
            if self.n - 1 - self.sl[-1] > maxi:
                pos = self.n - 1
                maxi = self.n - 1 - self.sl[-1]
        self.sl.add(pos)
        return pos

    def leave(self, p: int) -> None:
        self.sl.remove(p)