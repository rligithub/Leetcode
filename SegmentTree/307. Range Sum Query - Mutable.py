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


class NumArray1:  # binary index tree

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


class TreeNode:
    def __init__(self, val, start, end):  # start ~ end ==> interval range
        self.val = val
        self.start, self.end = start, end  # get interval range of node
        self.left, self.right = None, None  # get children nodes


class SegmentTree:
    def __init__(self, n):
        self.root = self.buildTree(0, n - 1)

    def buildTree(self, L, R):
        if L > R:
            return R
        root = TreeNode(0, L, R)
        if L == R:
            return root
        mid = L + (R - L) // 2
        root.left = self.buildTree(L, mid)
        root.right = self.buildTree(mid + 1, R)

        return root

    def update(self, i, diff, root=None):  # from top to the end
        root = root or self.root
        if i < root.start or i > root.end:
            return
        root.val += diff
        if i == root.start == root.end:  # [1,1] OR [99, 99] ---> only one num
            return

        self.update(i, diff, root.left)
        self.update(i, diff, root.right)

    def query(self, L, R, root=None):
        root = root or self.root
        if R < root.start or L > root.end:
            return 0

        if L <= root.start and R >= root.end:
            return root.val
        return self.query(L, R, root.left) + self.query(L, R, root.right)


class NumArray:  # segment tree

    def __init__(self, nums: List[int]):
        self.tree = SegmentTree(len(nums))
        self.nums = nums
        for i, num in enumerate(nums):
            self.tree.update(i, num)

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.tree.update(index, delta)
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.query(left, right)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)