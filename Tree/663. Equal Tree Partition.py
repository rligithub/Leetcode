# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    # Wrong solution --> Global variable record value for (left, left + right, left + right + root)
    # but in here, left can not be with right without root
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        self.prefsum = []
        self.summ = 0
        self.dfs(root)
        print(self.prefsum)
        self.prefsum.pop()
        if self.summ / 2 in self.prefsum:
            return True
        else:
            return False

    def dfs(self, root):
        if not root:
            return 0
        self.dfs(root.left)
        self.dfs(root.right)
        self.summ += root.val
        self.prefsum.append(self.summ)


class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:

        self.visited = []
        summ = self.dfs(root)
        # print(self.sum)
        if summ / 2 != summ // 2:
            return False
        self.visited.pop()
        target = summ // 2
        return target in self.visited

    def dfs(self, root):
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)
        summ = left + right + root.val  # local variable, each level append (left + right + val)
        self.visited.append(summ)
        return summ



