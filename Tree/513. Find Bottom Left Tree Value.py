# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # BFS --> print path for first node of each level --> return path[-1]
        queue = collections.deque()
        queue.append(root)
        res = []

        while queue:
            size = len(queue)

            for i in range(size):
                cur = queue.popleft()
                if i == 0:
                    res.append(cur.val)

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return res[-1]


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # DFS --> compare maxdepth --> get left node of maxdepth --> pre-order
        res = []

        self.left = None
        self.maxdepth = 0
        self.dfs(root, 0)
        if self.left:
            return self.left.val
        else:
            return root.val

    def dfs(self, root, depth):
        if not root:
            return
        if not root.left and not root.right and depth > self.maxdepth:  # 叶子节点并且 深度最深 pre-order
            self.maxdepth = depth
            self.left = root

        self.dfs(root.left, depth + 1)
        self.dfs(root.right, depth + 1)
