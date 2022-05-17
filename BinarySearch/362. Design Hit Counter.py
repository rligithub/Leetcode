class HitCounter1:

    def __init__(self):
        self.time = []

    def hit(self, timestamp: int) -> None:
        self.time.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        if not self.time:
            return 0

        n = len(self.time)

        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if self.time[mid] > timestamp - 300:  # find right boundary
                right = mid - 1
            else:
                left = mid + 1
        return n - left


class HitCounter:

    def __init__(self):
        self.time = []

    def hit(self, timestamp: int) -> None:
        self.time.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        if not self.time:
            return 0
        pos = bisect.bisect_right(self.time, timestamp - 300)
        return len(self.time) - pos

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)