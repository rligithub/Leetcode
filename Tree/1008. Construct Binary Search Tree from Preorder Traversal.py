# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # use preorder to build BST
        # NOTE THAT idx of preorder will always ++

        self.pos = 0
        return self.dfs(preorder, float('-inf'), float('inf'))

    def dfs(self, preorder, minn, maxx):
        if self.pos == len(preorder):
            return None

        val = preorder[self.pos]
        if val < minn or val > maxx:
            return None
        self.pos += 1
        root = TreeNode(val)
        root.left = self.dfs(preorder, minn, val)
        root.right = self.dfs(preorder, val, maxx)
        return root