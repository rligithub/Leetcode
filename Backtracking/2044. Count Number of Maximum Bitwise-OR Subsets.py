class Solution1:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # pick or not pick

        # step1: get max possible bitwise OR

        maxx = 0
        for i in nums:
            maxx = maxx | i

        # step2: get combination from nums and make the bitwise OR equal to max bit
        self.count = 0
        self.dfs(nums, maxx, 0, 0)
        return self.count

    def dfs(self, nums, target, pos, mask):
        if pos == len(nums):
            if mask == target:
                self.count += 1
            return

        self.dfs(nums, target, pos + 1, mask | nums[pos])
        self.dfs(nums, target, pos + 1, mask)


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # similar to combination summ ---> combination OR == target
        maxx = 0
        for i in nums:
            maxx = maxx | i

        self.res = 0
        self.dfs(nums, maxx, 0, 0)
        return self.res

    def dfs(self, nums, maxx, mask, pos):
        if mask > maxx:
            return

        if mask == maxx:
            self.res += 1

        for i in range(pos, len(nums)):
            self.dfs(nums, maxx, mask | nums[i], i + 1)


