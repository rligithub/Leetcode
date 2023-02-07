class FreqStack:

    def __init__(self):
        self.freq = collections.Counter()  # {num1: freq1, num2: freq2}
        self.group = collections.defaultdict(list)  # {freq: num1, num2, num3...}
        self.maxfreq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        f = self.freq[val]
        self.maxfreq = max(self.maxfreq, f)  # update maxx freq
        self.group[f].append(val)

    def pop(self) -> int:
        num = self.group[self.maxfreq].pop()  # choose 1 from list of num with max freq, pop
        self.freq[num] -= 1  # update freq

        if not self.group[self.maxfreq]:  # check if there is num for max freq --> if not, update maxfreq
            self.maxfreq -= 1
        return num

    # Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()