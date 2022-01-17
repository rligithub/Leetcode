# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution3:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.res = 0
        self.dfs(root, 0, distance)
        return self.res

    def dfs(self, root, depth, target):
        if not root:
            return []

        if not root.left and not root.right:  # 每次返回左右孩子的【深度】list --> 深度为从root到叶子节点的距离
            return [depth]

        leftleaf = self.dfs(root.left, depth + 1, target)
        rightleaf = self.dfs(root.right, depth + 1, target)

        for left in leftleaf:
            for right in rightleaf:
                if left + right - 2 * depth <= target:  # root到左右叶子节点的距离和 - 最小公共祖先到root的距离*2 ==> 两个叶子节点的距离
                    self.res += 1

        return leftleaf + rightleaf


class Solution2:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        dic = collections.defaultdict(TreeNode)
        leaves = []
        # find parent and all leaf nodes
        self.dfs(root, None, leaves, dic)

        self.res = 0
        for node in leaves:
            self.dfs2(node, 0, [node], distance, leaves, dic)
        return self.res // 2

    def dfs(self, root, parent, leaves, dic):
        if not root:
            return

        if not root.left and not root.right:
            leaves.append(root)
        dic[root] = parent
        self.dfs(root.left, root, leaves, dic)
        self.dfs(root.right, root, leaves, dic)

    def dfs2(self, root, dist, visited, distance, leaves, dic):
        if dist > distance:
            return

        if dist <= distance and root in leaves and root not in visited:
            self.res += 1

        if root.left and root.left not in visited:
            self.dfs2(root.left, dist + 1, visited + [root], distance, leaves, dic)
        if root.right and root.right not in visited:
            self.dfs2(root.right, dist + 1, visited + [root], distance, leaves, dic)
        if dic[root] and dic[root] not in visited:
            self.dfs2(dic[root], dist + 1, visited + [root], distance, leaves, dic)


class Solution1:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        neighbors = collections.defaultdict(list)
        leaves = []
        # cerate neighbors and all leaf nodes
        self.dfs(root, None, leaves, neighbors)

        self.res = 0
        for node in leaves:
            self.dfs2(node, 0, [node], distance, leaves, neighbors)
        return self.res // 2

    def dfs(self, root, parent, leaves, neighbors):
        if not root:
            return

            # add leaves
        if not root.left and not root.right:
            leaves.append(root)
        # build graph for neighbors
        neighbors[root].append(parent)
        neighbors[parent].append(root)

        self.dfs(root.left, root, leaves, neighbors)
        self.dfs(root.right, root, leaves, neighbors)

    def dfs2(self, root, dist, visited, distance, leaves, neighbors):
        if dist > distance:
            return

        if dist <= distance and root in leaves and root not in visited:
            self.res += 1

        for nei in neighbors[root]:
            if nei not in visited:
                self.dfs2(nei, dist + 1, visited + [root], distance, leaves, neighbors)


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        # similar to #863 all nodes distance k in binary tree --> only one target's neighbor nodes with k distance --> print neighbor
        # but this is getting many leaf_node's neighbor leaf_node with k distance --> how many pairs
        neighbors = collections.defaultdict(list)
        leaves = []
        # cerate neighbors and all leaf nodes
        self.dfs(root, None, leaves, neighbors)

        self.res = 0
        self.path = []
        for node in leaves:
            self.res += self.bfs(node, 0, set(), distance, leaves, neighbors)
        return self.res // 2

    def dfs(self, root, parent, leaves, neighbors):
        if not root:
            return

            # add leaves
        if not root.left and not root.right:
            leaves.append(root)
        # build graph for neighbors
        neighbors[root].append(parent)
        neighbors[parent].append(root)

        self.dfs(root.left, root, leaves, neighbors)
        self.dfs(root.right, root, leaves, neighbors)

    def bfs(self, root, dist, visited, k, leaves, neighbors):
        queue = collections.deque()
        queue.append(root)
        visited.add(root)
        res = 0

        while queue:
            size = len(queue)
            for i in range(size):
                cur = queue.popleft()
                if cur and 0 < dist <= k and cur in leaves:  # 必须是下一个叶子节点 + 距离不能为0 或超过 k
                    res += 1
                    self.path.append(cur.val)
                if dist > k:
                    break
                for nei in neighbors[cur]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)

            dist += 1
        return res




