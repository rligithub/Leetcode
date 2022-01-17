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

        return maxx  % (10 ** 9 + 7)

    def dfs(self, root):
        if not root:
            return 0

        summL = self.dfs(root.left)
        summR = self.dfs(root.right)
        summTotal = root.val + summL + summR

        self.res.append(summTotal)
        return summTotal


class Solution2:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # two summ --> find max product of two num

        self.res = []
        total = self.dfs(root)

        maxx = float('-inf')
        for num in self.res:
            maxx = max(maxx, num * (total - num))
        return maxx % (10 ** 9 + 7)

    def dfs(self, root):
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        summ = left + right + root.val
        self.res.append(summ)
        return summ


class SolutionTony:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        self.res = float('-inf')
        self.findSum(root)
        self.dfs(root)
        return self.res % (10 ** 9 + 7)

    def dfs(self, node):
        if not node:
            return 0

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        summ = left + right + node.val
        self.res = max(self.res, summ * (self.sum - summ))
        return left + right + node.val

    def findSum(self, node):
        if not node:
            return

        self.sum += node.val
        self.findSum(node.left)
        self.findSum(node.right)