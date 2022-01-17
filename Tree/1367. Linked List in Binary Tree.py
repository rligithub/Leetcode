# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            return True

        if not root:
            return False
        return self.dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def dfs(self, head, node):
        # if we got all values in linkedlist, then we good
        if not head:
            return True
        # no more tree node values, then False
        if not node:
            return False

        if node.val != head.val:
            return False
        else:
            return self.dfs(head.next, node.left) or self.dfs(head.next, node.right)