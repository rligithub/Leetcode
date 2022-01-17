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


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        isBST, minn, maxx = self.dfs(root)
        return isBST

    def dfs(self, root):
        if not root:
            return True, float('inf'), float('-inf')

        lBST, lminn, lmaxx = self.dfs(root.left)
        rBST, rminn, rmaxx = self.dfs(root.right)

        minn = min(lminn, root.val)
        maxx = max(rmaxx, root.val)
        isBST = lmaxx < root.val < rminn and lBST and rBST
        return isBST, minn, maxx
