class TrieNode:
    def __init__(self):
        self.one = None
        self.zero = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            if num & (1 << i):
                if not node.one:
                    node.one = TrieNode()
                node = node.one
            else:
                if not node.zero:
                    node.zero = TrieNode()
                node = node.zero

    def search(self, num):
        node = self.root
        xor = 0
        for i in range(31, -1, -1):
            isNum = num & (1 << i)
            if node.one and not isNum:  # if cur is zero --> choose 1 --> return 1
                node = node.one
                xor += 1 << i
            elif node.zero and isNum:  # if cur is one --> choose 0 --> return 1
                node = node.zero
                xor += 1 << i
            else:
                node = node.one or node.zero
        return xor


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        if not nums:
            return 0

        trie = Trie()
        for num in nums:
            trie.insert(num)

        res = 0
        for num in nums:
            res = max(res, trie.search(num))
        return res