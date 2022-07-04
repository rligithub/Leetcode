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
            if num & (1 << i):  # 1
                if not node.one:
                    node.one = TrieNode()
                node = node.one
            else:  # 0
                if not node.zero:
                    node.zero = TrieNode()
                node = node.zero

    def search(self, num):
        node = self.root
        xor = 0
        for i in range(31, -1, -1):
            bit = num & (1 << i)

            if bit and node.zero:  # cur 1, need 0
                node = node.zero
                xor += 1 << i
            elif not bit and node.one:  # cur 0, need 1
                node = node.one
                xor += 1 << i
            else:
                node = node.one or node.zero

        return xor


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()

        for i, query in enumerate(queries):
            queries[i] = [i, query]

        queries = sorted(queries, key=lambda x: x[1][1])
        trie = Trie()
        res = [-1] * len(queries)
        j = 0

        for i, (x, m) in queries:
            while j < len(nums) and nums[j] <= m:
                trie.insert(nums[j])
                j += 1
            if j == 0:  # 如果没有比m小的数字，即trie为空 --> 不用search, skip
                continue
            res[i] = trie.search(x)

        return res







