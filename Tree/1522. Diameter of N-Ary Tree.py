"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""


class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """

        # similar to #1245 TREE DIAMETER
        # each nodes return longest depth, diameter == longest and second longest

        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return 0
        max1, max2 = 0, 0

        for child in root.children:
            count = self.dfs(child)

            if count > max1:
                max2 = max1
                max1 = count

            elif count > max2:
                max2 = count

        self.res = max(self.res, max1 + max2)

        return max1 + 1