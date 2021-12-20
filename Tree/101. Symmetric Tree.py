# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 类似题#100 same tree ==》 从大到小来看 是对称的 -> root.left == root.right, root.right == root.left
        if not root:
            return True

        return self.dfs(root.left, root.right)

    def dfs(self, a, b):
        if not a and not b:
            return True

        if not a or not b:
            return False

        l2r = self.dfs(a.left, b.right)
        r2l = self.dfs(a.right, b.left)

        return a.val == b.val and l2r and r2l