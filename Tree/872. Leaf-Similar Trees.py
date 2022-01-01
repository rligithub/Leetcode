# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:  # DFS --> print path, then compare
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        res1 = []
        res2 = []
        return self.dfs(root1, res1) == self.dfs(root2, res2)

    def dfs(self, root, res):
        if not root:
            return

        if not root.left and not root.right:
            res.append(root.val)

        self.dfs(root.left, res)
        self.dfs(root.right, res)
        return res

