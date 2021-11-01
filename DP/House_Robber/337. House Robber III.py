# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:  # top down dp
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        return self.dfs(root, memo)

    def dfs(self, root, memo):
        if root in memo:
            return memo[root]

        # base case
        if not root:
            return 0

        # rob
        rob = root.val
        if root.left:
            rob += self.dfs(root.left.left, memo) + self.dfs(root.left.right, memo)
        if root.right:
            rob += self.dfs(root.right.left, memo) + self.dfs(root.right.right, memo)

        # not_rob
        not_rob = self.dfs(root.left, memo) + self.dfs(root.right, memo)

        memo[root] = max(rob, not_rob)
        return memo[root]


class Solution:  # dfs
    def rob(self, root: Optional[TreeNode]) -> int:
        res = self.dfs(root)
        return max(res[0], res[1])

    def dfs(self, root):
        # base case
        if not root:
            return 0, 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        rob = root.val + left[0] + right[0]
        not_rob = max(left[0], left[1]) + max(right[0], right[1])

        return not_rob, rob