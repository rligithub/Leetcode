class Solution:
    def rob(self, nums: List[int]) -> int:
        # res = max value of rob house
        # for cur_house i --> rob vs not rob
        # CASE 1: if rob house i, next rob can only be house i + 2
        # CASE 2: if not rob house i, next rob can be house i + 1

        memo = {}
        return self.dfs(nums, 0, memo)

    def dfs(self, nums, pos, memo):
        if pos in memo:
            return memo[pos]

        # base case --> 只要 之前 pos+1 / pos + 2 大于最后的房子（len -1）== > 0
        if pos > len(nums) - 1:
            return 0

        # rob vs not_rob
        not_rob = self.dfs(nums, pos + 1, memo)
        rob = self.dfs(nums, pos + 2, memo) + nums[pos]

        memo[pos] = max(rob, not_rob)
        return memo[pos]