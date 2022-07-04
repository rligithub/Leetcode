# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.root = head

    def getRandom(self) -> int:

        cur = self.root
        i = 1
        res = -1
        while cur:
            if random.random() < 1 / i:
                res = cur.val
            cur = cur.next
            i += 1
        return res

    # Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()