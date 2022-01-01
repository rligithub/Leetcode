# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.summ = 0
        self.dfs(root)
        return root

    def dfs(self, root):
        if not root:
            return 0

        self.dfs(root.right)
        self.summ += root.val
        root.val = self.summ
        self.dfs(root.left)