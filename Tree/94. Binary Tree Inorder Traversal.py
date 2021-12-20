# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:  # DFS - recurisive
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


class Solution2:  # iterative
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        stack = []
        cur = root

        # put left nodes
        while cur:
            stack.append(cur)
            cur = cur.left

        while stack:
            cur = stack.pop()
            res.append(cur.val)
            # check if any right nodes --> append --> check if any left nodes
            if cur.right:
                cur = cur.right
                while cur:
                    stack.append(cur)
                    cur = cur.left
        return res


class SolutionTony:
    def inorderTraversal(self, root):
        if not root:
            return []

        stack = [root]
        res = []

        while stack:
            node = stack.pop()
            if isinstance(node, int):
                res.append(node)
                continue

            if node.right:  # if has right node, push into stack
                stack.append(node.right)
            stack.append(node.val)  # Push VALUE into stack, in between left and right
            if node.left:  # if has left node, push into stack
                stack.append(node.left)

        return res