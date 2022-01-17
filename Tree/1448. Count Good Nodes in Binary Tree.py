# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # root to any nodes, last node must be >= max(all prev nodes)
        self.res = 0
        self.dfs(root, float('-inf'))
        return self.res

    def dfs(self, root, maxx):
        if not root:
            return

        maxx = max(maxx, root.val)

        if root.val >= maxx:
            self.res += 1

        self.dfs(root.left, maxx)
        self.dfs(root.right, maxx)pre