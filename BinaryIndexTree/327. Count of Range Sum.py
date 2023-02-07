class BinaryIndexTree:
    def __init__(self, n):
        self.freq = [0] * (n + 1)

    def lowbit(self, x):
        return x & (-x)

    def update(self, i, val):
        while i < len(self.freq):
            self.freq[i] += val
            i += self.lowbit(i)

    def query(self, i):
        res = 0
        while i > 0:
            res += self.freq[i]
            i -= self.lowbit(i)
        return res


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # get prefSum
        prefSum = [0]
        for num in nums:
            prefSum.append(prefSum[-1] + num)

        tree = BinaryIndexTree(len(prefSum))
        sortedSum = sorted(
            prefSum)  # 把prefSum按顺序排列， 如果该summ出现，则在tree里的位置标记frequency +1，然后求prefix summ的 prefsum的frequency

        res = 0
        for summ in prefSum:  # lower < summ1 - summ2 < upper
            right = bisect.bisect_right(sortedSum, summ - lower)  # summ2 < summ1 - lower
            left = bisect.bisect_left(sortedSum, summ - upper)  # summ2 > summ1 - upper
            res += tree.query(right) - tree.query(left)

            pos = bisect.bisect_right(sortedSum, summ)
            tree.update(pos, 1)

        return res