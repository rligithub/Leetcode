class Solution1:  # TLE
    def largestComponentSize(self, nums: List[int]) -> int:
        n = len(nums)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if self.hasCommonFactor(nums[i], nums[j]):
                    uf.union(i, j)

        count = collections.defaultdict(int)

        for i in range(n):
            p = uf.find(i)
            count[p] += 1
        return max(count.values())

    def hasCommonFactor(self, a, b):
        for i in range(2, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                return True
        return False


class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])

        return self.parent[i]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)

        if rootA != rootB:
            self.parent[rootA] = rootB


class Solution2:
    def largestComponentSize(self, nums: List[int]) -> int:
        n = max(nums) + 1
        uf = UnionFind(n)
        for num in nums:
            for factor in range(2, int(math.sqrt(num)) + 1):
                if num % factor == 0:
                    uf.union(num, factor)
                    uf.union(num, num // factor)
        print(uf.parent)
        count = collections.defaultdict(int)

        for num in nums:
            p = uf.find(num)
            count[p] += 1
        return max(count.values())


class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])

        return self.parent[i]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)

        if rootA != rootB:
            self.parent[rootA] = rootB


class Solution:  # save space
    def largestComponentSize(self, nums: List[int]) -> int:

        uf = UnionFind()
        for num in nums:
            for factor in range(2, int(math.sqrt(num)) + 1):
                if num % factor == 0:
                    uf.union(num, factor)
                    uf.union(num, num // factor)
        count = collections.defaultdict(int)

        for num in nums:
            p = uf.find(num)
            count[p] += 1

        return max(count.values())


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
