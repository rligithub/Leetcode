# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:  # faster
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.res = [root.val]

        self.left(root.left)
        self.leaves(root, root)
        self.right(root.right)

        return self.res

    def left(self, root):
        if not root or not root.left and not root.right:
            return

        self.res.append(root.val)
        if root.left:
            self.left(root.left)
        else:
            self.left(root.right)

    def leaves(self, node, root):
        if not node:
            return
        self.leaves(node.left, root)
        if node != root and not node.left and not node.right:
            self.res.append(node.val)

        self.leaves(node.right, root)

    def right(self, root):
        if not root or not root.left and not root.right:
            return
        if root.right:
            self.right(root.right)
        else:
            self.right(root.left)

        self.res.append(root.val)


class Solution:  # slower
    def boundaryOfBinaryTree(self, root):

        if not root:
            return []
        self.res = [root.val]
        self.dfs(root.left, True, False)
        self.dfs(root.right, False, True)
        return self.res

    def dfs(self, root, isleft, isright):
        if root:
            # append when going down from the left or at leaf node
            if (not root.left and not root.right) or isleft:
                self.res.append(root.val)

            if root.left and root.right:
                self.dfs(root.left, isleft, False)
                self.dfs(root.right, False, isright)
            else:
                self.dfs(root.left, isleft, isright)
                self.dfs(root.right, isleft, isright)

            # append to boundary when coming up from the right
            if (root.left or root.right) and isright:
                self.res.append(root.val)


