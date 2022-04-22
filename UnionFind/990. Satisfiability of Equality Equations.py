class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind()

        for equation in equations:
            if equation[1:3] == '==':
                uf.union(equation[0], equation[3])

        for equation in equations:
            if equation[1:3] == '!=':
                if uf.find(equation[0]) == uf.find(equation[3]):
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
