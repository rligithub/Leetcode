# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # any node to any nodes--> top to down
        res = []
        path = []

        self.call(root, res, targetSum)
        return len(res)

    def call(self, root, res, targetSum):
        if not root:
            return
        self.dfs(root, targetSum, 0, [], res)
        self.call(root.left, res, targetSum)
        self.call(root.right, res, targetSum)

    def dfs(self, root, targetSum, summ, path, res):
        if not root:
            return []

        if summ + root.val == targetSum:
            res.append(path + [root.val])

        self.dfs(root.left, targetSum, summ + root.val, path + [root.val], res)
        self.dfs(root.right, targetSum, summ + root.val, path + [root.val], res)

        return res


class Solution3:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0

        self.call(root, targetSum)
        return self.res

    def call(self, root, targetSum): # pick any start points
        if not root:
            return 0
        self.dfs(root, targetSum, 0)
        self.call(root.left, targetSum)
        self.call(root.right, targetSum)

    def dfs(self, root, targetSum, summ): # print path
        if not root:
            return 0

        if summ + root.val == targetSum:
            self.res += 1

        self.dfs(root.left, targetSum, summ + root.val)
        self.dfs(root.right, targetSum, summ + root.val)

        return self.res


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        return self.dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)

    def dfs(self, root, targetSum):
        if not root:
            return 0

        left = self.dfs(root.left, targetSum - root.val)
        right = self.dfs(root.right, targetSum - root.val)

        return left + right + int(root.val == targetSum)

