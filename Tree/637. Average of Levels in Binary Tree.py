# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # get average value of nodes on each level --> BFS
        if not root:
            return []
        queue = collections.deque()
        res = []
        queue.append(root)

        while queue:
            size = len(queue)
            level = 0
            count = 0
            for i in range(size):
                cur = queue.popleft()
                level += cur.val
                count += 1
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            res.append(level / count)
        return res 