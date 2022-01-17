# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return float('inf'), float('-inf'), True, 0

        Lmin, Lmax, LBST, Lsumm = self.dfs(root.left)
        Rmin, Rmax, RBST, Rsumm = self.dfs(root.right)

        isBST = LBST and RBST and Lmax < root.val < Rmin
        maxx = max(root.val, Rmax)
        minn = min(root.val, Lmin)
        summ = root.val + Lsumm + Rsumm

        if isBST:
            self.res = max(self.res, summ)

        return minn, maxx, isBST, summ


class Solution2:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root, float('inf'), float('-inf'))
        return self.res

    def dfs(self, root, minn, maxx):
        if not root:
            return float('inf'), float('-inf'), 0

        Lmin, Lmax, Lsumm = self.dfs(root.left, minn, root.val - 1)
        Rmin, Rmax, Rsumm = self.dfs(root.right, root.val + 1, maxx)

        if Lmax < root.val < Rmin:
            summ = Lsumm + Rsumm + root.val
            self.res = max(self.res, summ)
            return min(Lmin, root.val), max(Rmax, root.val), summ

        return float('-inf'), float('inf'), 0


class Solution3:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return float('inf'), float('-inf'), 0

        Lmin, Lmax, Lsumm = self.dfs(root.left)
        Rmin, Rmax, Rsumm = self.dfs(root.right)

        if Lmax < root.val < Rmin:
            summ = Lsumm + Rsumm + root.val
            self.res = max(self.res, summ)
            return min(Lmin, root.val), max(Rmax, root.val), summ

        return float('-inf'), float('inf'), 0

