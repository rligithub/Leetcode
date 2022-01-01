# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # save summ of each subtree --> get total summ of whole tree  --> get max(summ*(totalsum - summ))
        self.res = []

        # return total summ + record sub summ of each subtree
        total = self.dfs(root)

        maxx = 0
        for num in self.res:
            maxx = max(maxx, num * (total - num))

        return maxx

    def dfs(self, root):
        if not root:
            return 0

        summL = self.dfs(root.left)
        summR = self.dfs(root.right)
        summTotal = root.val + summL + summR

        self.res.append(summTotal)
        return summTotal
