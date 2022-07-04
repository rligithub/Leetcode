class Solution1:  # non-recursive
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        prev, cur = None, head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev


class Solution:  # recursive
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.dfs(None, head)

    def dfs(self, prev, cur):
        if not cur:
            return prev

        nxt = cur.next
        cur.next = prev
        return self.dfs(cur, nxt)


