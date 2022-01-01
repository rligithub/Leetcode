"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def intersect(self, qt1: 'Node', qt2: 'Node') -> 'Node':
        # QuadTree1 OR QuadTree2
        # 四叉树 --> 对于每个nodes只可能是 (val, isLeaf) --> (1, 1), (1, 0), (0, 1) --> 不可能有（0, 0）的情况出现

        # 如果都是叶子节点 --> (1, 1) or (0, 1)
        if qt1.isLeaf and qt2.isLeaf:
            return Node(qt1.val or qt2.val, True)

        # 如果只有一个是叶子节点 (1,1)
        if (qt1.isLeaf and qt1.val) or (qt2.isLeaf and qt2.val):
            return Node(True, True)

        tl = self.intersect(qt1.topLeft or qt1, qt2.topLeft or qt2)
        tr = self.intersect(qt1.topRight or qt1, qt2.topRight or qt2)
        bl = self.intersect(qt1.bottomLeft or qt1, qt2.bottomLeft or qt2)
        br = self.intersect(qt1.bottomRight or qt1, qt2.bottomRight or qt2)

        children = [tl, tr, bl, br]
        values = [child.val for child in children]
        leaves = [child.isLeaf for child in children]

        if all(leaves) and (sum(values) == 0 or sum(values) == 4):
            return Node(True, True)

        return Node(False, False, tl, tr, bl, br)


class Solution1:
    def intersect(self, qt1: 'Node', qt2: 'Node') -> 'Node':
        # 对于每个nodes只可能是 (val, isLeaf) --> (1, 1), (1, 0), (0, 1) --> 不可能有（0, 0）的情况出现

        # 如果只有一个是叶子节点 (1,1) 或者 (0,1)
        if qt1.isLeaf:
            if qt1.val:  # qt1 (1, 1) --> 1--> return 1
                return qt1
            else:  # qt1 (0, 1) --> 0 --> return qt2
                return qt2
        if qt2.isLeaf:
            if qt2.val:
                return qt2
            else:
                return qt1

        tl = self.intersect(qt1.topLeft, qt2.topLeft)
        tr = self.intersect(qt1.topRight, qt2.topRight)
        bl = self.intersect(qt1.bottomLeft, qt2.bottomLeft)
        br = self.intersect(qt1.bottomRight, qt2.bottomRight)

        children = [tl, tr, bl, br]
        values = [child.val for child in children]
        leaves = [child.isLeaf for child in children]

        # 如果是叶子节点 且 有相同的值 ---> (1, 1)
        if all(leaves) and (sum(values) == 0 or sum(values) == 4):
            return Node(True, True, None, None, None, None)

        # non-leaf must have False val
        return Node(False, False, tl, tr, bl, br)