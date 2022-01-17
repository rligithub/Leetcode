# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:

        count, minn, maxx = self.dfs(root)
        return count

    def dfs(self, root):
        if not root:
            return 0, float("inf"), float("-inf")

        lcount, lmin, lmax = self.dfs(root.left)
        rcount, rmin, rmax = self.dfs(root.right)

        if lmax < root.val < rmin:  # BST
            return lcount + rcount + 1, min(lmin, root.val), max(rmax, root.val)  # 看能否和root组合成一个大的

        return max(lcount, rcount), float("-inf"), float("inf")  # 只能选一边


class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:

        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return True, 0, float("inf"), float("-inf")

        lBST, lcount, lmin, lmax = self.dfs(root.left)
        rBST, rcount, rmin, rmax = self.dfs(root.right)

        isBST = lBST and rBST and lmax < root.val < rmin
        maxx = max(root.val, rmax)
        minn = min(root.val, lmin)
        count = lcount + rcount + 1

        if isBST:
            self.res = max(self.res, count)
        return isBST, count, minn, maxx
