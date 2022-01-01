# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        # swap left and right if preorder doesn't tie with voyage
        # Note that voyage is moving forward alway --> use global variable

        self.res = []
        self.pos = 0
        if self.dfs(root, voyage):
            return self.res
        else:
            return [-1]

    def dfs(self, root, voyage):
        if not root:
            return True

        if root.val != voyage[self.pos]:
            return False

        self.pos += 1
        if root.left and root.left.val == voyage[self.pos]:
            return self.dfs(root.left, voyage) and self.dfs(root.right, voyage)
        elif root.right and root.right.val == voyage[self.pos]:
            if root.left:
                self.res.append(root.val)
            return self.dfs(root.right, voyage) and self.dfs(root.left, voyage)

        return not root.left and not root.right


class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        # swap left and right if preorder doesn't tie with voyage
        # Note that voyage is moving forward alway --> use global variable

        self.res = []
        self.pos = 0
        self.dfs(root, voyage, None)
        if self.pos == len(voyage):
            return self.res
        else:
            return [-1]

    def dfs(self, root, voyage, parent):
        if not root:
            return
        if not parent and root.val != voyage[self.pos]:
            return

        if root.val != voyage[self.pos]:
            parent.left, parent.right = parent.right, parent.left  # swap
            if parent.left and parent.left.val == voyage[self.pos]:
                self.res.append(parent.val)
                root = parent.left
            else:
                return

        self.pos += 1

        self.dfs(root.left, voyage, root)
        self.dfs(root.right, voyage, root)

