# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # 求哪一层是maxsum --> BFS

        res = float('-inf')
        count = 0
        cnt = 0
        queue = collections.deque()
        queue.append(root)

        while queue:
            size = len(queue)
            level = 0
            for i in range(size):
                cur = queue.popleft()
                level += cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            cnt += 1

            if res < level:
                res = level
                count = cnt
        return count 