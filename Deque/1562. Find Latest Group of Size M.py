class Solution1:  # Deque
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if n == m:
            return n
        arr.insert(0, 0)
        res = -1

        day = {}
        for i in range(1, n + 1):
            day[arr[i]] = i

        queue = collections.deque()

        for i in range(1, n + 1):
            while queue and i - queue[0] >= m:
                queue.popleft()

            # maintain lastest step in queue[0]
            while queue and day[i] > day[queue[-1]]:
                queue.pop()

            queue.append(i)
            if i < m:
                continue

            left, right = float('inf'), float('inf')
            if i - m >= 1:
                left = day[i - m]  # 检查左边是不是为 0
            if i + 1 <= n:
                right = day[i + 1]  # 检查右边是不是为 0
            if day[queue[0]] < left and day[queue[0]] < right:
                res = max(res, min(left, right) - 1)

        return res


class Solution:  # union find
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if m == n: return n

        uf = UnionFind(n)

        res = -1
        for i, pos in enumerate(arr):
            uf.sizes[pos] = 1
            for nei in (pos - 1, pos + 1):
                if 0 < nei < n + 1 and uf.sizes[nei] > 0:
                    if uf.sizes[uf.find(nei)] == m:
                        res = i
                    uf.union(nei, pos)
        return res


class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n + 1)]
        self.sizes = [0 for i in range(n + 1)]

    def find(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        self.sizes[rootA] += self.sizes[rootB]
        self.parents[rootB] = rootA
        return self.sizes[rootA]

