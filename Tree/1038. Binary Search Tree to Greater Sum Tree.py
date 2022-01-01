# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # same to #538
        # change the root.val to new value --> return root
        self.summ = 0
        self.dfs(root)
        return root

    def dfs(self, root):  # in-order accumulate --> right + root + left
        if not root:
            return

        self.dfs(root.right)
        self.summ += root.val
        root.val = self.summ
        self.dfs(root.left)

