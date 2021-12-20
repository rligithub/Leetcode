# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # BFS --> need to find left node and left node must be leaf nodes
        queue = collections.deque()
        res = 0

        queue.append(root)

        while queue:
            size = len(queue)

            for i in range(size):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                    if not cur.left.left and not cur.left.right:
                        res += cur.left.val
                if cur.right:
                    queue.append(cur.right)
        return res


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # DFS --> if it's left leaf nodes, return val ++
        # root.left --> YES left nodes
        # root.right --> NO left nodes
        return self.dfs(root, False)

    def dfs(self, root, leftNode):
        if not root:
            return 0

        if not root.left and not root.right:
            if leftNode:
                return root.val
            else:
                return 0

        return self.dfs(root.left, True) + self.dfs(root.right, False)


