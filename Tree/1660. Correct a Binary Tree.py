# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        # BFS --> if is cur.left or cur.right in visited --> error --> delete cur
        if not root:
            return

        queue = collections.deque()

        visited = set()
        queue.append(root)
        visited.add(root)

        while queue:
            cur = queue.popleft()
            if cur.right:
                if cur.right.right in visited:
                    cur.right = None
                    return root
                else:
                    queue.append(cur.right)
                    visited.add(cur.right)
            if cur.left:
                if cur.left.right in visited:
                    cur.left = None
                    return root
                else:
                    queue.append(cur.left)
                    visited.add(cur.left)

        return root


class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        queue = collections.deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if node.right:
                if node.right.right in queue:
                    node.right = None
                    return root
                else:
                    queue.append(node.right)
            if node.left:
                if node.left.right in queue:
                    node.left = None
                    return root
                else:
                    queue.append(node.left)
        return root