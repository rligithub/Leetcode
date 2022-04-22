class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # connect all equivalent char
        uf = UnionFind()
        for i in range(len(s1)):
            uf.union(s1[i], s2[i])

        # find the smallest root and replace it
        res = ''
        for ch in baseStr:
            root = uf.find(ch)
            res += root
        return res


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
            if ord(rootA) < ord(rootB):  # 注意把小的字母作为root
                rootA, rootB = rootB, rootA
            self.parent[rootA] = rootB