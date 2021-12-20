# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # vertifical --> make root as 0, root.left as -1, root.right as 1
        # 只能用bfs 因为 dfs打印path不一定能使得top to bottom

        # 赋值 add index --> hashmap

        if not root:
            return
        table = collections.defaultdict(list)
        queue = collections.deque()
        queue.append([0, root])

        while queue:
            size = len(queue)

            for i in range(size):
                idx, cur = queue.popleft()
                table[idx].append(cur.val)

                if cur.left:
                    queue.append([idx - 1, cur.left])
                if cur.right:
                    queue.append([idx + 1, cur.right])

        res = []
        for i in sorted(table.keys()):
            res.append(table[i])
        return res


