# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS --> only return last node in each level, top to down
        if not root:
            return []

        res = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            size = len(queue)

            for i in range(size):
                cur = queue.popleft()

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(cur.val)
        return res


class Solution: # DFS
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        self.res = []

        self.dfs(root, 0)
        return self.res

    def dfs(self, root, level):
        if not root:
            return

        if level >= len(self.res): # 一层一个 
            self.res.append(root.val)

        self.dfs(root.right, level + 1)
        self.dfs(root.left, level + 1)