# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution1:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # dfs --> find parent and depth --> compare both

        px, dx = self.dfs(root, None, 0, x)
        py, dy = self.dfs(root, None, 0, y)

        return dx == dy and px != py

    def dfs(self, node, parent, depth, target):
        if not node:
            return
        if node.val == target:
            return parent, depth
        return self.dfs(node.left, node, depth + 1, target) or self.dfs(node.right, node, depth + 1, target)


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # bfs --> find two parents, compare
        queue = collections.deque()
        queue.append((root, None))

        while queue:
            size = len(queue)
            found_one = False
            p_one = None
            for i in range(size):
                cur, p = queue.popleft()
                if cur.val == x or cur.val == y:
                    if not found_one:
                        found_one = True
                        p_one = p
                    else:
                        return p_one != p

                if cur.left:
                    queue.append((cur.left, cur))
                if cur.right:
                    queue.append((cur.right, cur))
        return False

