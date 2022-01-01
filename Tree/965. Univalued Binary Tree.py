# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        self.val = root.val
        return self.dfs(root)

    def dfs(self, root):
        if not root:
            return True

        if root.val != self.val:
            return False

        return self.dfs(root.left) and self.dfs(root.right)
