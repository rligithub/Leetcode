class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # 一个node对应两个 "#" --> count代表#还能有几个
        preorder = preorder.split(',')
        count = 1
        n = len(preorder)
        for i, node in enumerate(preorder):
            if node == '#':
                count -= 1
            else:
                count += 1
            # i < n - 1 means we still have node after #, which is not correct
            if count == 0 and i < n - 1:
                return False
        return count == 0
