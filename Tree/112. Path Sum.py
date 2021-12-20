# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        # root 为空的话，题目的意思是要返回 False 的
        if not root:
            return False

            # 子节点 必须要算上最后一个子节点的value
        if not root.left and not root.right and targetSum - root.val == 0:
            return True

        left = self.hasPathSum(root.left, targetSum - root.val)
        right = self.hasPathSum(root.right, targetSum - root.val)

        return left or right

