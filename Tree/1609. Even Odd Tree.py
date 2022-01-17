# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        # BFS -->
        # odd level: even val decreasing from left to right
        # even level: odd val increasing from left to right

        queue = collections.deque()
        queue.append(root)
        level = 0

        while queue:
            size = len(queue)
            prev = -1
            for i in range(size):
                cur = queue.popleft()
                if level % 2 == cur.val % 2:
                    return False
                if prev != -1:
                    if level % 2 == 0 and cur.val <= prev:
                        return False
                    if level % 2 != 0 and cur.val >= prev:
                        return False
                prev = cur.val

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            level += 1

        return True


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = collections.deque()
        queue.append((root, 0))

        while queue:
            size = len(queue)
            prev = -1
            for i in range(size):
                cur, level = queue.popleft()
                if level % 2 == cur.val % 2:
                    return False
                if prev != -1:
                    if level % 2 == 0 and cur.val <= prev:
                        return False
                    if level % 2 != 0 and cur.val >= prev:
                        return False
                prev = cur.val

                if cur.left:
                    queue.append((cur.left, level + 1))
                if cur.right:
                    queue.append((cur.right, level + 1))

        return True