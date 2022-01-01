# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:

        return self.dfs(root, target)

    def dfs(self, root, target):
        if not root:
            return None, None

        elif root.val <= target:
            small, large = self.dfs(root.right, target)
            root.right = small  # 断开比target大的root
            return root, large

        elif root.val > target:
            small, large = self.dfs(root.left, target)
            root.left = large  # 上一层root脸上比target大的node
            return small, root




