class UnionFind:
    def __init__(self):
        self.parent = defaultdict(str)
        self.rank = defaultdict(set)

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x

        if x not in self.rank:
            self.rank[x].add(x)

        if self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]

        return self.parent[x]

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx == rooty:
            return
        if rootx > rooty:
            rootx, rooty = rooty, rootx
            x, y = y, x
        self.parent[rooty] = rootx
        self.rank[rootx] |= self.rank[rooty]


class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        uf = UnionFind()
        for w1, w2 in synonyms:
            uf.union(w1, w2)

        self.table = {}
        for word in uf.parent:
            root = uf.find(word)
            self.table[root] = sorted(list(uf.rank[root]))

        self.textlist = text.split(' ')
        self.ans = []
        self.backtrack(uf, 0, '')
        return self.ans

    def backtrack(self, uf, i, path):
        if i == len(self.textlist):
            self.ans += path.lstrip(' '),
            return
        word = self.textlist[i]
        if word in uf.parent:
            root = uf.find(word)
            for alt in self.table[root]:
                self.backtrack(uf, i + 1, path + ' ' + alt)
        else:
            self.backtrack(uf, i + 1, path + ' ' + word)