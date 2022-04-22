class Solution:  # union find
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # union all equations together + save values（存的值为 = ch/root_ch） as well
        alphabet = set(sum(equations, []))
        uf = UnionFind(alphabet)

        for val, (num1, num2) in zip(values, equations):
            uf.union(val, num1, num2)
        # for loop queries ---> check if u, v are connected, if not return -1, if yes, return res
        res = []
        for x, y in queries:
            if x not in alphabet or y not in alphabet:  # CASE1 --> one/all nums not in equations
                res.append(-1)
                continue
            rootX, valX = uf.find(x)
            rootY, valY = uf.find(y)
            if rootX != rootY:  # CASE2 --> two nums are not connnected
                res.append(-1)
            else:
                res.append(valX / valY)  # CASE3 --> two nums are connected
        return res


class UnionFind():
    def __init__(self, alphabet):
        self.parent = {ch: ch for ch in alphabet}
        self.vals = {ch: 1 for ch in alphabet}  # 存的值为 = ch/root_ch

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i], val = self.find(self.parent[i])
            self.vals[i] *= val
        return self.parent[i], self.vals[i]

    def union(self, val, a, b):
        rootA, valA = self.find(a)
        rootB, valB = self.find(b)
        if rootA != rootB:
            self.parent[rootA] = rootB
            self.vals[rootA] = val * valB / valA













