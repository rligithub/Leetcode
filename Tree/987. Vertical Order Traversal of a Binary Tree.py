# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # similar to #314 Binary tree vertical order travel
        # but need to sort value if it's in same level
        if not root:
            return []
        table = []

        queue = collections.deque()
        queue.append((root, 0, 0))

        while queue:
            cur, index, lvl = queue.popleft()
            table.append((index, lvl, cur.val))

            if cur.left:
                queue.append((cur.left, index - 1, lvl + 1))
            if cur.right:
                queue.append((cur.right, index + 1, lvl + 1))

        res = collections.defaultdict(list)

        for index, lvl, value in sorted(table):
            res[index].append(value)
        return res.values()


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []
        self.dfs(root, 0, 0)

        ans = collections.defaultdict(list)

        for index, lvl, value in sorted(self.res):
            ans[index].append(value)
        return ans.values()

    def dfs(self, root, depth, col):
        if not root:
            return 0
        self.res.append((col, depth, root.val))
        left = self.dfs(root.left, depth + 1, col - 1)
        right = self.dfs(root.right, depth + 1, col + 1)

