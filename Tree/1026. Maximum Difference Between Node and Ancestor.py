# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return float('inf'), float('-inf')

        leftmin, leftmax = self.dfs(root.left)
        rightmin, rightmax = self.dfs(root.right)

        minn = min(leftmin, rightmin, root.val)
        maxx = max(leftmax, rightmax, root.val)

        self.res = max(self.res, abs(root.val - maxx), abs(root.val - minn))

        return minn, maxx


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return float('inf'), float('-inf')

        if not root.left and not root.right:
            return root.val, root.val

        leftmin, leftmax = self.dfs(root.left)
        rightmin, rightmax = self.dfs(root.right)

        self.res = max(self.res, abs(root.val - min(leftmin, rightmin)), abs(root.val - max(leftmax, rightmax)))

        minn = min(leftmin, rightmin, root.val)
        maxx = max(leftmax, rightmax, root.val)

        return minn, maxx


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        self.dfs(root, root.val, root.val)
        return self.res

    def dfs(self, root, minn, maxx):
        if not root:
            self.res = max(self.res, abs(maxx - minn))
            return

        minn = min(minn, root.val)
        maxx = max(maxx, root.val)

        self.dfs(root.left, minn, maxx)
        self.dfs(root.right, minn, maxx)
