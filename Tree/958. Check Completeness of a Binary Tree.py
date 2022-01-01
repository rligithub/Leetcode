# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # BFS --> if level == "#", append to res --> if res and cur: return False

        if not root:
            return True

        queue = collections.deque()
        queue.append(root)
        res = []

        while queue:
            cur = queue.popleft()

            if not res and not cur:
                res.append('#')
            if res and cur:
                return False

            if cur:
                queue.append(cur.left)
                queue.append(cur.right)

        return True