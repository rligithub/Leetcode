# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        # similar to #298 print longest consecutive path --> any nodes to any nodes
        # but not required to be parent to child, can be reverse

        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return [0, 0]

        increase, decrease = 1, 1

        if root.left:
            inL, deL = self.dfs(root.left)
            if root.left.val == root.val - 1:
                decrease = max(decrease, deL + 1)
            if root.left.val == root.val + 1:
                increase = max(increase, inL + 1)

        if root.right:
            inR, deR = self.dfs(root.right)
            if root.right.val == root.val - 1:
                decrease = max(decrease, deR + 1)
            if root.right.val == root.val + 1:
                increase = max(increase, inR + 1)

        self.res = max(self.res, increase + decrease - 1)
        return [increase, decrease]

