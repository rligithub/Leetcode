'''
for example:

pre: 3,9,8,11,20,15,7
     R - - -  -  -  -

in:  8,9,11,3,15,20,7
     - - -  R -  -  -

post:8,11,9,15,7,20,3
     - -  - -  - -  R


'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder[-1])
        idx = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[:idx + 1], postorder[:idx])
        root.right = self.buildTree(inorder[idx + 1:], postorder[idx:-1])

        return root


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None

        return self.dfs(inorder, postorder, 0, len(inorder) - 1, 0, len(postorder) - 1)

    def dfs(self, inorder, postorder, inleft, inright, postleft, postright):

        if postright < 0 or inleft > inright:
            return None

        root = TreeNode(postorder[postright])
        idx = inorder.index(postorder[postright])

        size = idx - inleft
        root.left = self.dfs(inorder, postorder, inleft, idx - 1, postleft, postleft + size - 1)
        root.right = self.dfs(inorder, postorder, idx + 1, inright, postleft + size, postright - 1)

        return root




