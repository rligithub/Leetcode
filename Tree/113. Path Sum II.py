# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # similar to #112 path sum --> but return all valid path
        # 注意：思路一模一样，最后一个叶子节点需要加上叶子节点的路径

        res = []
        path = []
        return self.dfs(root, targetSum, path, res)

    def dfs(self, root, targetSum, path, res):
        if not root:
            return res

        if not root.left and not root.right and targetSum - root.val == 0:
            res.append(path + [root.val])

        left = self.dfs(root.left, targetSum - root.val, path + [root.val], res)
        right = self.dfs(root.right, targetSum - root.val, path + [root.val], res)

        return res