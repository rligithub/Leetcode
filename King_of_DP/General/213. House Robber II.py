class Solution:
    def rob(self, nums: List[int]) -> int:
        # circled house + regular house robber
        # circled ==> can't rob adjacent house --> two scenarios: rob nums[1:] and rob nums[:-1]

        # edge case (n == 1)
        # recursive start (n >= 2)

        # n == 1:
        if len(nums) == 1:
            return nums[0]
        # n >= 2:
        memo1 = {}
        memo2 = {}
        return max(self.dfs(nums[1:], 0, memo1), self.dfs(nums[:-1], 0, memo2))

    def dfs(self, nums, pos, memo):
        if pos in memo:
            return memo[pos]

        if pos > len(nums) - 1:
            return 0

        # rob vs not_rob
        memo[pos] = max(self.dfs(nums, pos + 2, memo) + nums[pos], self.dfs(nums, pos + 1, memo))

        return memo[pos]