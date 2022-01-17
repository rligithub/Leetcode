# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS
        # Step 1. BFS to get the lowest level's nodes.
        # As we do BFS, create a link to a parent.
        parent = collections.defaultdict(TreeNode)
        queue = collections.deque()
        queue.append(root)

        while queue:
            size = len(queue)
            level = set()
            for i in range(size):
                cur = queue.popleft()
                level.add(cur)

                if cur.left:
                    queue.append(cur.left)
                    parent[cur.left] = cur
                if cur.right:
                    queue.append(cur.right)
                    parent[cur.right] = cur
            # Step 2: Move upward from children to parents until there is
            # only one parent. This parent is the LCA.
        while len(level) > 1:
            pp = set()
            for node in level:
                pp.add(parent[node])
            level = pp
        return list(level)[0]


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # DFS 返回的是以root为根节点的树的最深深度叶子节点的LCA，以及最大深度

        node, depth = self.dfs(root, 0)
        return node

    def dfs(self, root, depth):
        if not root:
            return None, depth

        leftnode, leftdepth = self.dfs(root.left, depth + 1)
        rightnode, rightdepth = self.dfs(root.right, depth + 1)

        if leftdepth == rightdepth:
            return root, leftdepth

        elif leftdepth > rightdepth:
            return leftnode, leftdepth
        else:
            return rightnode, rightdepth



