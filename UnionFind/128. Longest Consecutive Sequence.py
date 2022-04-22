class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 把当前num 的 连续consecutive sequence 和当前num ---> union 起来， 更新之前的{} 使得{i+1:i} or {i-1:i}
        if not nums:
            return 0

        parent = {}

        for num in nums:
            if num not in parent:
                parent[num] = num
                if num - 1 in parent:
                    self.union(parent, num - 1, num)
                if num + 1 in parent:
                    self.union(parent, num + 1, num)
        print(parent)

        count = collections.defaultdict(int)
        for num in parent:
            p = self.find(parent, num)
            count[p] += 1
        print(count)
        return max(count.values())

    def find(self, parent, i):
        if parent[i] == i:
            return i

        return self.find(parent, parent[i])

    def union(self, parent, a, b):
        rootA = self.find(parent, a)
        rootB = self.find(parent, b)
        if rootA != rootB:
            parent[rootA] = rootB

