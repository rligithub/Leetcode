# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # BST
        if not root:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if root == p or root == q:
            return root
        if left and right:
            return root
        if not left and not right:
            return None
        if not left or not right:
            return left or right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return

        if root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)

        if root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)

        return root