from sortedcontainers import SortedDict, SortedSet, SortedList

class SummaryRanges:

    def __init__(self):
        self.data = SortedList()

    def addNum(self, val: int):
        k = self.data.bisect_left([val, val])
        n = len(self.data)
        # if k-1's ending value already covered val or k-th value is val, then we don't need to insert
        #  ------    ----
        #     val or val
        if (k and val <= self.data[k-1][1]) or (k < n and self.data[k][0] == val):
            return
        # if previous ending + 1 < val and k-th starting > val + 1, then we insert (automatically sorted)
        # ---         ---
        #      -----
        if (k == 0 or self.data[k-1][1]+1 < val) and (k == n or val+1 < self.data[k][0]):
            self.data.add([val, val])
        # then it merge to
        # -----
        #      -
        # ------
        elif k and self.data[k-1][1]+1 == val:
            self.data[k-1][1] += 1
            # ---- ----
            #     -
            # ---------
            if k < n and val+1 == self.data[k][0]:
                self.data[k-1][1] = self.data.pop(k)[1]
        #  ----
        # -
        # -----
        elif k < n and val+1 == self.data[k][0]:
            self.data[k][0] -= 1

    def getIntervals(self) -> List[List[int]]:
        return list(self.data)
# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()


