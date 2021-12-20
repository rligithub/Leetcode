# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        return self.dfs(root, None, None)

    def dfs(self, root, left, right):
        if not root:
            return left

        res = self.dfs(root.left, root, root.right)

        root.left = right
        root.right = left

        return res


class Solution:  # prefer
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or not root.left:
            return root

        res = self.upsideDownBinaryTree(root.left)

        root.left.left = root.right
        root.left.right = root
        root.left = None
        root.right = None

        return res