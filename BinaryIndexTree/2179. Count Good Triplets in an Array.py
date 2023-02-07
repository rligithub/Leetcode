"""
index         0 1 2 3 4
nums1         4 0 1 3 2 ---> for loop num in nums1, from left to right --> left side means past, i means cur, right side means future
                  i

tree(nums2)   4 1 0 2 3     ---> check if appearing order in nums2 is the same --> left means past, i means cur, right means future
value(appear) X   X
                i

good triplets --> show order as past->cur->future ===> left side appears(past), nums1[i] (cur), right side unappears(future)

res += left_appear * right_unappear

"""


class BinaryIndexTree:
    def __init__(self, n):
        self.count = [0] * (n + 1)

    def lowbit(self, x):
        return x & (-x)

    def update(self, i, val):
        while i < len(self.count):
            self.count[i] += val
            i += self.lowbit(i)

    def query(self, i):
        res = 0
        while i > 0:
            res += self.count[i]
            i -= self.lowbit(i)
        return res


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # 三个数字 出现的顺序 在nums1和nums2 要一样 --> good Triplets ， 和数字value本身没有关系
        # step1： 先把nums2的index都存起来
        # step2： 每for loop一个num在nums1，以当前num为triplets的中心，在tree里该num对应nums2中index 左边已经出现的个数 和 右边还没出现的个数， res += left*right

        index = {}
        for i, num in enumerate(nums2):
            index[num] = i + 1

        n = len(nums1)
        tree = BinaryIndexTree(n)
        res = 0

        for i, num in enumerate(nums1):  # tree里存的是index:对应的数字的nums2的index， value是nums2位置上已经出现的数字个数
            pos2 = index[num]
            left_count = tree.query(pos2)  # find appeared count for nums2 in tree 找已经出现过的nums2的当前i的左边count
            right_count = n - pos2 - (tree.query(n) - tree.query(pos2))  # 还未出现的总个数 - 出现在右边的个数
            res += left_count * right_count

            tree.update(pos2, 1)
        return res

