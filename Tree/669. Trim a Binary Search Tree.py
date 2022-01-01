# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # 给一个范围 --> 删掉范围外的nodes 使之还是BST
        # 3 CASES：
        # 1）在范围内 --> 返回root
        # 2）< 范围 ---> 左孩子肯定不在范围内，裁掉，返回右孩子
        # 3) > 范围 ---> 右孩子肯定不在范围内，裁掉，返回左孩子
        return self.dfs(root, low, high)

    def dfs(self, root, low, high):
        if not root:
            return None
        root.left = self.dfs(root.left, low, high)
        root.right = self.dfs(root.right, low, high)

        if root.val < low:  # 左边剪掉，返回右孩子 -->左边肯定不在范围内，返回右孩子在范围内
            return root.right
        if root.val > high:  # 右边剪掉，返回左孩子 --> 以root.left为根节点返回
            return root.left

        return root  # 在范围内,返回root
