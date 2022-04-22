class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        # edge case
        if len(sentence1) != len(sentence2):
            return False

            # union all similar paris together
        uf = UnionFind()
        for word1, word2 in similarPairs:
            uf.union(word1, word2)

        # for loop sentence1 and sentence2 to see if word1 and word2 are connected --> return False if not
        for i in range(len(sentence1)):
            root1 = uf.find(sentence1[i])
            root2 = uf.find(sentence2[i])
            if root1 != root2:
                return False
        return True


class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, i):
        if i not in self.parent:
            self.parent[i] = i
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA != rootB:
            self.parent[rootA] = rootB