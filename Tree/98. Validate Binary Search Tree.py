# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.dfs(root, float('-inf'), float('inf'))

    def dfs(self, root, minn, maxx):
        if not root:
            return True

        left = self.dfs(root.left, minn, root.val)
        right = self.dfs(root.right, root.val, maxx)

        return minn < root.val < maxx and left and right