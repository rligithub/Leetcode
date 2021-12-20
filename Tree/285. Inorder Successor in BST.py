# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        # BST !!!
        self.res = None
        self.dfs(root, p)
        return self.res

    def dfs(self, root, p):
        if not root:
            return None

        self.dfs(root.left, p)
        if root.val > p.val and not self.res:  # find first node.val > p.val, use "not self.res" to make sure this is the first value
            self.res = root
            return  # early termination, find first value already, no need to check right nodes

        self.dfs(root.right, p)
