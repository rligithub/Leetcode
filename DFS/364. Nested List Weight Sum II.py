# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        # similar to 339 Nested List Weight Sum --> BUT reverse depth 123 --> 321
        # use hashmap to save each depth and its num --> {depth : num }
        hashmap = collections.defaultdict(list)
        self.maxdepth = 0

        self.dfs(nestedList, 1, hashmap)

        res = 0
        for depth in hashmap:
            for num in hashmap[depth]:
                res += num * (self.maxdepth - depth + 1)
        return res

    def dfs(self, nums, depth, hashmap):

        for num in nums:
            if num.isInteger():
                self.maxdepth = max(self.maxdepth, depth)
                hashmap[depth].append(num.getInteger())
            else:
                self.dfs(num.getList(), depth + 1, hashmap)











