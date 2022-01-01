# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # BST --> prev node must be global variable --> in order
        self.prev = float('inf')
        self.res = float('inf')
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return

        self.dfs(root.left)

        self.res = min(self.res, abs(root.val - self.prev))
        self.prev = root.val

        self.dfs(root.right)