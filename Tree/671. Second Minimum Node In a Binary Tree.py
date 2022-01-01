# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        # 找第二小的node.val

        self.min1 = float('inf')
        self.min2 = float('inf')

        self.dfs(root)
        if self.min2 < float('inf'):
            return self.min2
        else:
            return -1

    def dfs(self, root):
        if not root:
            return

        if root.val < self.min1:
            self.min2 = self.min1
            self.min1 = root.val
        if self.min1 < root.val < self.min2:
            self.min2 = root.val

        self.dfs(root.left)
        self.dfs(root.right)