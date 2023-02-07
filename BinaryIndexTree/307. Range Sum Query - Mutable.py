class BinaryIndexTree:
    def __init__(self, n):
        self.summ = [0] * (n + 1)

    def _lowbit(self, x):
        return x & (-x)

    def update(self, i, delta):
        while i < len(self.summ):
            self.summ[i] += delta
            i += self._lowbit(i)

    def query(self, i):
        res = 0
        while i:
            res += self.summ[i]
            i -= self._lowbit(i)
        return res


class NumArray:  # binary index tree

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.tree = BinaryIndexTree(len(nums))
        for i, num in enumerate(nums):  # build tree
            self.tree.update(i + 1, num)

    def update(self, index: int, val: int) -> None:
        self.tree.update(index + 1, val - self.nums[index])  # update prefsumm in tree
        self.nums[index] = val  # update nums

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.query(right + 1) - self.tree.query(left)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)