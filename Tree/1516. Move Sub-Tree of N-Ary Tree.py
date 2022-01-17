"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""


class Solution1:
    def moveSubTree(self, root: 'Node', p: 'Node', q: 'Node') -> 'Node':
        # 要把 p 移成 q的最右边孩子
        lca = self.dfs(root, p, q)

        dummy_root = Node(0)
        dummy_root.children.append(root)
        par = {}
        self.find_parent(None, dummy_root, par)

        # case 1 --> 符合题意，公共祖先为q
        if lca == q:
            if p in q.children:  # 直系--> 直接返回root
                return root
            else:
                par[p].children.remove(p)  # 非直系 --> 断开连接p的parent，把p作为子孩子连上q
                q.children.append(p)

        # case 2  --> 公共祖先为p
        elif lca == p:
            par[q].children.remove(q)  # 先断开q的parent --> 把p作为子孩子连上q
            q.children.append(p)

            for index, n in enumerate(par[p].children):  # 找出p的parent和p对应的位置，断开并replace它为q
                if n == p:
                    par[p].children[index] = q

        # case 3 --> 左右两边
        else:
            par[p].children.remove(p)  # 断开p的parent
            q.children.append(p)  # 把p作为子孩子连上q

        return dummy_root.children[0]

    def dfs(self, root, p, q):
        if not root:
            return None
        find = []
        for child in root.children:
            ans = self.dfs(child, p, q)
            if ans:
                find.append(ans)  # append p and q

        if root == p or root == q:  # base case
            return root

        if len(find) == 1:  # left or right
            return find[0]
        elif len(find) == 2:  # left and right
            return root
        else:
            return None  # not left and not right

    def find_parent(self, parent, root, par):
        if not root:
            return
        par[root] = parent
        for child in root.children:
            self.find_parent(root, child, par)