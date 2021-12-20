# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        # 如果left和right只有一个为0，说明他只有一个子结点，我们只需要返回它另一个子节点的深度+1即可（不能选择深度最小的）
        if not left or not right:
            return left + right + 1

        # 如果left和right都不为0或者都为0，说明他有两个子节点，我们只需要返回最小深度的+1即可。
        return min(left, right) + 1