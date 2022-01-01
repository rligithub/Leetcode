# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # min path sum from leaf to root --> print path in str
        # postorder

        self.res = ''
        path = ''
        self.dfs(root, path)

        return self.res

    def dfs(self, root, path):
        if not root:
            return
        path = chr(root.val + 97) + path
        self.dfs(root.left, path)
        self.dfs(root.right, path)

        if not root.left and not root.right:
            if not self.res:
                self.res = path
            self.res = min(self.res, path)
        return root





