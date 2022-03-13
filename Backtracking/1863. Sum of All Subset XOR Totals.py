class Solution1:
    def subsetXORSum(self, nums: List[int]) -> int:
        # step1: get all subset
        # step2: get XOR of num in each subset
        # step3: summ of XOR

        self.res = 0
        self.dfs(nums, 0, [])
        return self.res

    def dfs(self, nums, pos, path):

        if path:
            ans = path[0]
            for j in range(1, len(path)):
                ans = ans ^ path[j]
            self.res += ans

        for i in range(pos, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]])


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = []
        n = len(nums)

        def dfs(i, xor):
            if i >= n:
                res.append(xor)
                return

            dfs(i + 1, xor)
            dfs(i + 1, xor ^ nums[i])

        dfs(0, 0)
        return sum(res)