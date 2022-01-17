# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.res = 1
        self.dfs(root, float('-inf'), 0)
        return self.res

    def dfs(self, root, prev, size):
        if not root:
            return

        if root.val == prev + 1:
            size += 1
            self.res = max(self.res, size)
        else:
            size = 1

        self.dfs(root.left, root.val, size)
        self.dfs(root.right, root.val, size)


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        # similar to #549, but path only from parent to child
        # 549 is for any node to any node
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return 0

        increase = 1

        if root.left:
            left = self.dfs(root.left)
            if root.left.val == root.val + 1:
                increase = max(increase, left + 1)

        if root.right:
            right = self.dfs(root.right)
            if root.right.val == root.val + 1:
                increase = max(increase, right + 1)

        self.res = max(self.res, increase)
        return increase


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.res = 1
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return 0

    def dfs(self, root):
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        L, R = 1, 1
        if root.left and root.left.val == root.val + 1:
            L = left + 1
        if root.right and root.right.val == root.val + 1:
            R = right + 1

        self.res = max(self.res, L, R)

        return max(L, R)

        return max(left, right)
