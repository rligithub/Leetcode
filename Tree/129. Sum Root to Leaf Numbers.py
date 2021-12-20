# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # similar to #124 (path sum - leaf to leaf)
        # this question is for path sum - root to leaf, root*10 + left, root*10 + right ==> left + right

        return self.dfs(root, 0)

    def dfs(self, root, res):
        if not root:
            return 0

        if not root.left and not root.right:
            return res * 10 + root.val

        left = self.dfs(root.left, res * 10 + root.val)
        right = self.dfs(root.right, res * 10 + root.val)

        return left + right