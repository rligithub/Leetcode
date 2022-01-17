# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        self.res = None
        self.dfs(original, cloned, target)
        return self.res

    def dfs(self, original, cloned, target):
        if not original or not cloned:
            return

        if original == target and cloned.val == original.val:
            self.res = cloned

        self.dfs(original.left, cloned.left, target)
        self.dfs(original.right, cloned.right, target)