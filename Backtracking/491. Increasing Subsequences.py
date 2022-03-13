class Solution:
    def findSubsequences(self, nums):
        # combination + increasing order
        res = []
        path = []
        self.dfs(nums, 0, path, res)
        return res

    def dfs(self, nums, pos, path, res):

        if len(path) >= 2:
            res.append(path)

        if pos >= len(nums):
            return

        visited = set()
        for i in range(pos, len(nums)):
            if nums[i] in visited:
                continue
            visited.add(nums[i])

            if not path or nums[i] >= path[-1]:
                self.dfs(nums, i + 1, path + [nums[i]], res)
nums = [0, 2, 2]
a = Solution()

print(a.findSubsequences(nums))