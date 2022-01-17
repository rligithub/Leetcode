# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        # 4 CASES:
        # 1) two child nodes
        # 2) leaf nodes
        # 3) only left nodes
        # 4) only right nodes

        # root.left --> add "("
        # root.right ---> add ")"

        return self.dfs(root)

    def dfs(self, root):
        if not root:
            return ''
        if not root.left and not root.right:
            return str(root.val) + ""
        elif not root.left:  # 只有左子树为空，返回 3()(2) 的形式
            return str(root.val) + '(' + ')' + '(' + self.dfs(root.right) + ')'
        elif not root.right:  # 只有右子树为空，返回 3(2)的形式
            return str(root.val) + '(' + self.dfs(root.left) + ')'
        else:  # 左右子树都不为空, 返回 3(2)(4) 的形式
            return str(root.val) + '(' + self.dfs(root.left) + ')' + '(' + self.dfs(root.right) + ')'


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        return self.dfs(root)

    def dfs(self, root):
        if not root:
            return ''
        val = str(root.val)
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if not root.left and not root.right:
            return val + ""

        elif not root.left:
            return val + '(' + ')' + '(' + right + ')'

        elif not root.right:
            return val + '(' + left + ')'

        else:
            return val + '(' + left + ')' + '(' + right + ')'