class BinaryIndexedTree:
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


class Solution1:  # Binary Indexed Tree + rank
    def createSortedArray(self, instructions: List[int]) -> int:
        n = max(instructions)
        mod = 10 ** 9 + 7
        res = 0
        tree = BinaryIndexedTree(n)
        for i, num in enumerate(instructions):
            left = tree.query(num - 1)
            right = i - tree.query(num)
            res = (res + min(left, right)) % mod

            tree.update(num, 1)
        return res


class Solution:  # Binary Indexed Tree + rank + 数据压缩（但是并没有影响，因为这道题的数据大小差不多）
    def createSortedArray(self, instructions: List[int]) -> int:
        # get compress of nums
        sortedNums = sorted(list(set(instructions)))
        index = {}
        for i, num in enumerate(sortedNums):
            index[num] = i + 1

        n = len(sortedNums)
        mod = 10 ** 9 + 7
        res = 0
        tree = BinaryIndexedTree(n)
        for i, num in enumerate(instructions):
            left = tree.query(index[num] - 1)
            right = i - tree.query(index[num])  # 已经出现的个数 i 减去多少个比num小的个数 ===> 多少个比num大的个数
            res = (res + min(left, right)) % mod

            tree.update(index[num], 1)
        return res
