# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.dfs(root, 0)
        return self.count

    def dfs(self, root, val):
        if not root:
            return True

        left = self.dfs(root.left, root.val)
        right = self.dfs(root.right, root.val)

        if not left or not right:
            return False
        self.count += 1#只有在true的时候才会++

        return root.val == val


class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.dfs(root)
        return self.count

    def dfs(self, root):
        if not root:
            return True

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if left and right and (not root.left or root.val == root.left.val) and (
                not root.right or root.val == root.right.val):
            self.count += 1
            return True

        return False

a = Solution1()
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(1)
root.left.right = TreeNode(8)
root.right.right = TreeNode(7)

print(a.countUnivalSubtrees(root))