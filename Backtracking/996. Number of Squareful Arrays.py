class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        # permutation

        self.res = 0
        nums = sorted(nums)
        self.dfs(nums, [], set())
        return self.res

    def dfs(self, nums, path, visited):

        if len(path) == len(nums):
            self.res += 1
            return

        for i in range(len(nums)):
            if i in visited:
                continue
            if i > 0 and nums[i] == nums[i - 1] and (i - 1) not in visited:
                continue
            if path and not self.isValid(path[-1] + nums[i]):
                continue
            visited.add(i)
            self.dfs(nums, path + [nums[i]], visited)
            visited.remove(i)

    def isValid(self, num):
        return int(sqrt(num)) == sqrt(num)