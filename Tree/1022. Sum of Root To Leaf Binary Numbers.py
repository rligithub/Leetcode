# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root, 0)
        return self.res

    def dfs(self, root, summ):
        if not root:
            return 0
        summ = (summ << 1) + root.val

        if not root.left and not root.right:
            self.res += summ

        self.dfs(root.left, summ)
        self.dfs(root.right, summ)