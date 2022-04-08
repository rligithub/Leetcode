# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        # maintenance一个deque来 存 所有不完全的节点（即下一个insert node的父节点）
        self.deque = collections.deque()
        self.root = root
        queue = collections.deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if not node.left or not node.right:  # 第一个不完全的节点 --> 下一个节点append位置的父节点
                self.deque.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def insert(self, val: int) -> int:
        node = self.deque[0]  # parent node
        self.deque.append(TreeNode(val))  # add new_node
        if not node.left:  # 如果parent node没有左孩子，则new_node为左孩子
            node.left = self.deque[-1]
        else:
            node.right = self.deque[-1]  # 如果parent node没有右孩子，则new_node为右孩子
            self.deque.popleft()  # pop parent node
        return node.val  # return parent val

    def get_root(self) -> Optional[TreeNode]:
        return self.root

    # Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()