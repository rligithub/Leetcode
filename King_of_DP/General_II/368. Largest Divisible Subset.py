class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # 找能被整除的最长序列 --> next_num = 1
        nums.sort()
        memo = {}
        return self.dfs(nums, 0, 1, memo)

    def dfs(self, nums, pos, nxt, memo):
        if (pos, nxt) in memo:
            return memo[(pos, nxt)]

        res = []
        for i in range(pos, len(nums)):
            if nums[i] % nxt == 0:
                path = [nums[i]] + self.dfs(nums, i + 1, nums[i], memo)
                if len(path) > len(res):
                    res = path
        memo[(pos, nxt)] = res
        return memo[(pos, nxt)]


