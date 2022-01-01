class Solution:  # BEST + preorder
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        # find unique root as main root --> save all leaves nodes --> find unique root not in leaves
        # save all root in hashmap {root.val: root}
        # construct new trees --> use hashmap to get next root --> check if BST and all roots are used
        # 存储all leaf node.val 的set
        leaves = set()
        # 存储 each root --> hashmap {node.val : node}
        subtree = dict()
        for root in trees:
            if root.left:
                leaves.add(root.left.val)
            if root.right:
                leaves.add(root.right.val)
            subtree[root.val] = root

        for root in trees:
            if root.val not in leaves:  # get unique root --> root of merged tree
                subtree.pop(root.val)  # remove it from subtree hashmap
                if self.dfs(subtree, root, float('-inf'), float('inf')) and not subtree:  # if build BTS and all subtree are used
                    return root
                else:
                    return None

        return None

    def dfs(self, subtree, root, minn, maxx):
        if not root:
            return True

        if minn >= root.val or root.val >= maxx:
            return False

        # if leaf nodes has the same value as root in subtree ---> merge
        if not root.left and not root.right and root.val in subtree:
            root.left = subtree[root.val].left
            root.right = subtree[root.val].right
            subtree.pop(root.val)  # remove root in subtree --> to ensure all subtrees are merged at the end

        return self.dfs(subtree, root.left, minn, root.val) and self.dfs(subtree, root.right, root.val, maxx)


class Solution2:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:

        m = {t.val: t for t in trees}
        c = Counter()
        for t in trees:
            if t.left:
                c[t.left.val] += 1
            if t.right:
                c[t.right.val] += 1
        if any(v > 1 for v in c.values()):
            return None

        roots = [t for t in trees if t.val not in c]
        if len(roots) != 1:
            return None
        root = m.pop(roots[0].val)

        if not self.build(m, root,  float('-inf'), float('inf')) or m:
            return None
        return root

    def build(self, subtree, root, minn, maxx):
        if (root.left and root.left.val < minn) or (root.right and root.right.val > maxx):
            return False

        if root.left and root.left.val in subtree:
            root.left = subtree[root.left.val]
            subtree.pop(root.left.val)

            if not self.build(subtree, root.left, minn, root.val):
                return False

        if root.right and root.right.val in subtree:
            root.right = subtree[root.right.val]
            subtree.pop(root.right.val)

            if not self.build(subtree, root.right, root.val, maxx):
                return False

        return True


class Solution1:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        # 存储all leaf node.val 的set
        leaves = set()
        # 存储 each root --> hashmap {node.val : node}
        subtree = dict()
        for root in trees:
            if root.left:
                leaves.add(root.left.val)
            if root.right:
                leaves.add(root.right.val)
            subtree[root.val] = root

        self.prev = float("-inf")

        for root in trees:
            if root.val not in leaves:  # get unique root --> root of merged tree
                subtree.pop(root.val)  # remove it from subtree hashmap
                if self.dfs(subtree, root) and not subtree:
                    return root
                else:
                    return None

        return None

    def dfs(self, subtree, root):
        if not root:
            return True

        # if leaf nodes has the same value as root in subtree ---> merge
        if not root.left and not root.right and root.val in subtree:
            root.left = subtree[root.val].left
            root.right = subtree[root.val].right
            subtree.pop(root.val)  # remove root in subtree --> to ensure all subtrees are merged at the end

        if not self.dfs(subtree, root.left):
            return False

        if root.val <= self.prev:
            return False
        self.prev = root.val

        return self.dfs(subtree, root.right)
