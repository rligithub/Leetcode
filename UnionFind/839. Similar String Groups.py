class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        # 求有几块 不相似的words --> 相似的连成一块 num of islands
        n = len(strs)

        uf = UnionFind()
        # step1: union
        for i in range(n):
            for j in range(i + 1, n):
                if self.isSmilar(strs[i], strs[j]):
                    uf.union(strs[i], strs[j])

        # step2: find
        visited = set()
        for word in strs:
            root = uf.find(word)
            if root not in visited:
                visited.add(root)
        return len(visited)

    def isSmilar(self, w1, w2):
        count = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                count += 1
            if count > 2:
                return False
        return True


class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, ch):
        if ch not in self.parent:
            self.parent[ch] = ch
        if self.parent[ch] != ch:
            self.parent[ch] = self.find(self.parent[ch])
        return self.parent[ch]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA != rootB:
            self.parent[rootA] = rootB

