# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # edge case --> add new root on top
        if depth == 1:
            p = TreeNode(val)
            p.left = root
            return p

        return self.dfs(root, val, depth, 1)

    def dfs(self, root, val, depth, count):
        if not root:
            return

        if count == depth - 1:
            childL = root.left
            childR = root.right
            root.left = TreeNode(val)
            root.right = TreeNode(val)
            root.left.left = childL
            root.right.right = childR

        self.dfs(root.left, val, depth, count + 1)
        self.dfs(root.right, val, depth, count + 1)
        return root

class Solution2: # BFS
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:

        if d == 1:
            newRoot = TreeNode(v)
            newRoot.left = root
            return newRoot

        queue = collections.deque()
        queue.append(root)

        for i in range(d - 2):
            size = len(queue)
            for j in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        while queue:
            node = queue.popleft()
            left = node.left
            node.left = TreeNode(v)
            node.left.left = left

            right = node.right
            node.right = TreeNode(v)
            node.right.right = right

        return root