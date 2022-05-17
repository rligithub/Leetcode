from sortedcontainers import SortedSet


class TimeMap:

    def __init__(self):
        self.wordTime = {}  # 获得每个word被set的时候的值

    def set(self, key: str, value: str, timestamp: int) -> None:  # {'foo': [[1, 4], ['bar', 'bar2']]}
        if key not in self.wordTime:
            self.wordTime[key] = [[timestamp], [value]]
        else:
            self.wordTime[key][0].append(timestamp)
            self.wordTime[key][1].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.wordTime:
            return ''
        times = self.wordTime[key][0]
        values = self.wordTime[key][1]

        if times[0] > timestamp:
            return ''

        pos = bisect_right(times, timestamp)
        return values[pos - 1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)