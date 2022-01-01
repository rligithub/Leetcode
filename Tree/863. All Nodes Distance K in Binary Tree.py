# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # similar to #742 Closest Leaf in a Binary Tree.py
        # 找离 target 距离为k的节点 --> 以 target 点为中心 向外扩散，找距离为k的nodes
        # DFS ---> if val == target, cerate neighbors
        neighbors = collections.defaultdict(list)

        self.dfs(root, None, neighbors)
        visited = set()
        queue = collections.deque()
        queue.append(target)
        visited.add(target)
        dist = 0
        res = []

        while queue:
            size = len(queue)

            for i in range(size):
                cur = queue.popleft()
                if cur and dist == k:
                    res.append(cur.val)
                for nei in neighbors[cur]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)

            dist += 1
        return res

    def dfs(self, root, parent, neighbors):
        if not root:
            return

        neighbors[root].append(parent)
        neighbors[parent].append(root)
        self.dfs(root.left, root, neighbors)
        self.dfs(root.right, root, neighbors)



