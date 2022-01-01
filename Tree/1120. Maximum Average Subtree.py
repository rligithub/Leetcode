# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        # get max average of subtree --> return count and summ of subtree
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return 0, 0

        summL, cntL = self.dfs(root.left)
        summR, cntR = self.dfs(root.right)

        summ = summL + summR + root.val
        cnt = cntL + cntR + 1

        self.res = max(self.res, summ / cnt)

        return summ, cnt 