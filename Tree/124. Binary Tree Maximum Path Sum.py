# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # path summ --> left leaf via bridge to right leaf ===> left + root + right
        if not root:
            return 0

        self.res = float('-inf')
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return 0

        left = max(self.dfs(root.left), 0)
        right = max(self.dfs(root.right), 0)

        self.res = max(self.res, left + right + root.val)
        return max(left, right) + root.val


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # path summ --> left leaf via bridge to right leaf ===> left + root + right
        if not root:
            return 0

        self.res = float('-inf')
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        self.res = max(self.res, left + right + root.val, left + root.val, right + root.val, root.val)
        return max(left, right, 0) + root.val