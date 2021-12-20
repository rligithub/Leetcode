# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        # similar to #236, but find LCA of a list of nodes instead of two nodes
        if not root:
            return root

        left = self.lowestCommonAncestor(root.left, nodes)
        right = self.lowestCommonAncestor(root.right, nodes)

        for node in nodes:
            if root == node:
                return root

        if left and right:
            return root
        if not left and not right:
            return None
        if left or right:
            return left or right


class Solution:  # optimaze
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        self.nodes = set(nodes)
        return self.dfs(root)

    def dfs(self, root):

        if not root:
            return root

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if root in self.nodes:
            return root

        if left and right:
            return root
        if not left and not right:
            return None
        if left or right:
            return left or right