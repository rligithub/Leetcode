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
class Solution1:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # similar to question #108 --> root is in the middle
        # find the middle of linkedlist --> two pointer --> slower and faster --> slower==mid, head == left, faster == right
        if not head:
            return None

        return self.dfs(head)

    def dfs(self, head):
        if not head:  # no listnode
            return None
        if not head.next:  # only one listnode
            return TreeNode(head.val)

        s = head
        f = head.next.next
        while f and f.next:
            s = s.next
            f = f.next.next

        mid = s.next  # s is prev of middle node
        s.next = None
        root = TreeNode(mid.val)

        root.left = self.dfs(head)
        root.right = self.dfs(mid.next)

        return root


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        mid = self.findmid(head)
        root = TreeNode(mid.val)

        if head == mid:
            return root

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)

        return root

    def findmid(self, head):
        prev = None
        s = f = head

        while f and f.next:
            prev = s
            s = s.next
            f = f.next.next

        if prev:
            prev.next = None

        return s
