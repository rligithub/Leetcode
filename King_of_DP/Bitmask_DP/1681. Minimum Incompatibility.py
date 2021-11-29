class Solution:
    def minimumIncompatibility(self, nums, k: int) -> int:

        memo = {}
        size = len(nums) // k  # the length of each partition
        res = self.dfs(tuple(nums), size, memo)  # turn the input into a tuple so the function can be cached
        return res if res != float('inf') else -1

    def dfs(self, nums, size, memo):
        if nums in memo:
            return memo[nums]

        if not nums:
            return 0

        res = float('inf')
        # choose a as a partition
        for comb in itertools.combinations(set(nums), size):
            remain = list(nums)
            for num in comb:
                remain.remove(num)
            res = min(res, max(comb) - min(comb) + self.dfs(tuple(remain), size, memo))

        memo[nums] = res
        return memo[nums]



