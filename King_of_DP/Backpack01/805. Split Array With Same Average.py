class Solution1:  # TLE
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        # 是否把数组分成两部分，使得 两部分的平均数相等
        # 平均数 = 总和 / 个数
        # if x/n == a/b     ===> (x-a)/(n-b) == a/b
        target = sum(nums)

        memo = {}
        return self.dfs(nums, target, 0, 0, 0, memo)

    def dfs(self, nums, target, pos, cursum, count, memo):
        if (pos, cursum, count) in memo:
            return memo[(pos, cursum, count)]

        if 0 < count < len(nums) and cursum * len(nums) == target * count:
            return True

        if pos >= len(nums):
            return False

        if self.dfs(nums, target, pos + 1, cursum + nums[pos], count + 1, memo):
            memo[(pos, cursum, count)] = True
            return True
        if self.dfs(nums, target, pos + 1, cursum, count, memo):
            memo[(pos, cursum, count)] = True
            return True

        memo[(pos, cursum, count)] = False
        return False


class Solution2:  # TLE
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        # 是否把数组分成两部分，使得 两部分的平均数相等
        # 平均数 = 总和 / 个数
        # if x/n == a/b     ===> (x-a)/(n-b) == a/b
        target = sum(nums)
        nums.sort()
        memo = {}
        return self.dfs(nums, target, 0, 0, 0, memo)

    def dfs(self, nums, target, pos, cursum, count, memo):
        if (pos, cursum, count) in memo:
            return memo[(pos, cursum, count)]

        if 0 < count < len(nums) and cursum * len(nums) == target * count:
            return True

        if pos >= len(nums):
            return False

        pick = self.dfs(nums, target, pos + 1, cursum + nums[pos], count + 1, memo)
        not_pick = 0
        i = pos
        while i < len(nums) and nums[i] == nums[pos]:
            i += 1
        not_pick = self.dfs(nums, target, i, cursum, count, memo)

        memo[(pos, cursum, count)] = pick or not_pick
        return memo[(pos, cursum, count)]


class Solution:  # OPTIMIZED
    def splitArraySameAverage(self, nums: List[int]) -> bool:

        total = sum(nums)
        n = len(nums)
        nums.sort()
        memo = {}
        for count in range(1, n):
            if total * count % n != 0:
                continue
            cursum = total * count / n
            if self.dfs(nums, 0, cursum, count, memo):
                return True
        return False

    def dfs(self, nums, pos, cursum, count, memo):
        if (pos, cursum, count) in memo:
            return memo[(pos, cursum, count)]

        if count == 0 and cursum == 0:
            return True

        if count == 0 and cursum == 0:
            return False
        if pos == len(nums):
            return False

        if self.dfs(nums, pos + 1, cursum - nums[pos], count - 1, memo):
            memo[(pos, cursum, count)] = True
            return True
        i = pos
        while i < len(nums) and nums[i] == nums[pos]:
            i += 1
        if self.dfs(nums, i, cursum, count, memo):
            memo[(pos, cursum, count)] = True
            return True

        memo[(pos, cursum, count)] = False
        return memo[(pos, cursum, count)]


class Solution:  # OPTIMIZED
    def splitArraySameAverage(self, nums: List[int]) -> bool:

        total = sum(nums)
        n = len(nums)
        nums.sort()
        memo = {}
        for count in range(1, n):
            if total * count % n == 0:
                cursum = total * count / n
                if self.dfs(nums, 0, cursum, count, memo):
                    return True
        return False

    def dfs(self, nums, pos, cursum, count, memo):
        if (pos, cursum, count) in memo:
            return memo[(pos, cursum, count)]

        if count == 0 and cursum == 0:
            return True

        if count == 0 or cursum == 0 or pos == len(nums):
            return False

        pick = self.dfs(nums, pos + 1, cursum - nums[pos], count - 1, memo)

        i = pos
        while i < len(nums) and nums[i] == nums[pos]:
            i += 1
        not_pick = self.dfs(nums, i, cursum, count, memo)

        memo[(pos, cursum, count)] = pick or not_pick
        return memo[(pos, cursum, count)]

