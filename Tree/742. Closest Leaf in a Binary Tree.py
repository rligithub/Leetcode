# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        # 找离 k最近的 叶子节点 --> 以 k 点为中心 向外扩散，找最近的leaf nodes
        # DFS ---> if val == k, crate neighbors

        neighbors = collections.defaultdict(list)
        self.dfs(root, None, neighbors)

        queue = collections.deque()
        visited = set()

        # k --> value of node, need to find node
        for node in neighbors:
            if node and node.val == k:
                queue.append(node)
                visited.add(node)

        while queue:
            cur = queue.popleft()
            if cur:
                if not cur.left and not cur.right:
                    return cur.val

                for nei in neighbors[cur]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)

    def dfs(self, root, parent, neighbors):
        if not root:
            return

        neighbors[root].append(parent)
        neighbors[parent].append(root)

        self.dfs(root.left, root, neighbors)
        self.dfs(root.right, root, neighbors)

