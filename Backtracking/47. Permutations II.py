class Solution:
    def permuteUnique(self, nums):
        # permutation with duplicated values, add visited set to de-duplicated
        res = []
        self.dfs(nums, 0, res)
        return res

    def dfs(self, nums, pos, res):
        if pos == len(nums):
            res.append(nums[:])
            return
        visited = set()
        for i in range(pos, len(nums)):
            # de-deuplicated
            if nums[i] in visited:
                continue
            visited.add(nums[i])

            nums[i], nums[pos] = nums[pos], nums[i]
            self.dfs(nums, pos + 1, res)
            nums[i], nums[pos] = nums[pos], nums[i]

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []
        # nums = sorted(nums)
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        visited = set()
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            visited.add(nums[i])
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums = sorted(nums)
        self.dfs(nums, [], res, set())
        return res

    def dfs(self, nums, path, res, visited):
        if len(path) == len(nums):
            res.append(path)
        for i in range(len(nums)):
            if i in visited:
                continue
            if i > 0 and nums[i] == nums[i-1] and (i-1) not in visited:
                continue
            visited.add(i)
            self.dfs(nums, path + [nums[i]], res, visited)
            visited.remove(i)


a = Solution()
nums = [2,2,1,1]
print(a.permuteUnique(nums))