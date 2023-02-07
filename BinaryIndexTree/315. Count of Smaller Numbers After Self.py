class BinaryIndexTree:
    def __init__(self, n):
        self.summ = [0] * (n + 1)

    def lowbit(self, x):
        return x & (-x)

    def update(self, i, val):
        while i < len(self.summ):
            self.summ[i] += val
            i += self.lowbit(i)

    def query(self, i):
        res = 0
        while i > 0:
            res += self.summ[i]
            i -= self.lowbit(i)

        return res


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # compress nums --> deduplicated
        allNums = sorted(list(set(nums)))

        index = {}
        for i, num in enumerate(allNums):
            index[num] = i + 1

        n = len(nums)
        res = [0] * n
        tree = BinaryIndexTree(n)

        for i in range(n - 1, -1, -1):
            res[i] = tree.query(index[nums[i]] - 1)
            tree.update(index[nums[i]], 1)  # BIT里存的是 如果当前数字nums[i]出现，则在该位置index[nums[i]]上标记为1，然后求prefsum, 即有几个数字小于当前数字
        return res

