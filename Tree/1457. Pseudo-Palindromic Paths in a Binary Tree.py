# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution2:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:

        hashset = set()
        self.res = 0
        self.dfs(root, hashset)
        return self.res

    def dfs(self, root, hashset):
        if not root:
            return

        if root.val not in hashset:
            hashset.add(root.val)
        else:
            hashset.remove(root.val)

        if not root.left and not root.right:
            if len(hashset) < 2:
                self.res += 1
        else:
            self.dfs(root.left, set(hashset))  # 每次新new一个hashset，用来backtracking --> 否则hashset里的值会一直改变
            self.dfs(root.right, set(hashset))


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:

        hashset = set()
        self.res = 0
        self.dfs(root, hashset)
        return self.res

    def dfs(self, root, hashset):
        if not root:
            return

        if root.val not in hashset:
            hashset.add(root.val)
        else:
            hashset.remove(root.val)

        if not root.left and not root.right:
            if len(hashset) < 2:
                self.res += 1

        self.dfs(root.left, hashset)
        self.dfs(root.right, hashset)

        # backtracking
        if root.val not in hashset:
            hashset.add(root.val)
        else:
            hashset.remove(root.val)


class Solution:
    def pseudoPalindromicPaths(self, root):
        # table = collections.defaultdict(int)
        table = set()
        return self.dfs(root, table)

    def dfs(self, node, table):
        if not node:
            return 0

        if node.val in table:
            table.discard(node.val)
        else:
            table.add(node.val)

        res = 0
        if node and not node.left and not node.right:
            if len(table) in [0, 1]:
                res += 1

        res += self.dfs(node.left, table) + self.dfs(node.right, table)
        if node.val in table:
            table.discard(node.val)
        else:
            table.add(node.val)
        return res


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        path = 0
        self.res = 0
        self.dfs(root, path)
        return self.res

    def dfs(self, root, path):
        if not root:
            return

        path = path ^ (1 << root.val)

        if not root.left and not root.right:
            if path & (path - 1) == 0:
                self.res += 1
            else:
                return

        self.dfs(root.left, path)
        self.dfs(root.right, path)