# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        queue = collections.deque()
        queue.append(root)

        while queue:
            size = len(queue)
            for i in range(size):
                cur = queue.popleft()

                if cur == u:
                    if i < size - 1:
                        return queue.popleft()
                    else:
                        return None

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
