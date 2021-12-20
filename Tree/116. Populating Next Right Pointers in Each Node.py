"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # BFS --> add next pointer to right pointers at same level
        if not root:
            return

        queue = collections.deque()
        queue.append(root)

        while queue:
            size = len(queue)

            for i in range(size):
                cur = queue.popleft()
                if queue:
                    cur.next = queue[0]

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            cur.next = None  # 必须放在for loop结尾，即每一层都遍历完了，最后一个node指向Null。如果放在for loop里面，则有可能cur.next会指向下一层新加入的node

        return root
