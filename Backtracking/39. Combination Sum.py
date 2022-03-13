class Solution1:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 打印所有组合使得sum为target，每个数可以用无限次。 pick or not pick
        path = []
        res = []

        self.dfs(candidates, target, 0, 0, res, path)
        return res

    def dfs(self, nums, target, i, summ, res, path):
        if summ > target:
            return

        if summ == target:
            res.append(path)
            return

        if i == len(nums):
            return

        self.dfs(nums, target, i, summ + nums[i], res, path + [nums[i]])

        self.dfs(nums, target, i + 1, summ, res, path)


class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 打印所有组合使得sum为target，每个数可以用无限次。
        path = []
        res = []

        self.dfs(candidates, target, 0, 0, res, path)
        return res

    def dfs(self, nums, target, pos, summ, res, path):
        if summ > target:
            return
        if summ == target:
            res.append(path)
            return

        for i in range(pos, len(nums)):
            self.dfs(nums, target, i, summ + nums[i], res, path + [nums[i]])


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 打印所有组合使得sum为target，每个数可以用无限次。 --> dfs for loop --> 先确定 当前这个数用几次，再决定后面的数用几次
        path = []
        res = []

        self.dfs(candidates, target, 0, 0, res, path)
        return res

    def dfs(self, nums, target, pos, summ, res, path):
        if summ > target:
            return
        if summ == target:
            print('summ == target:', path)
            res.append(path[:])
            return

        for i in range(pos, len(nums)):
            print(path)
            path.append(nums[i])
            self.dfs(nums, target, i, summ + nums[i], res, path)
            path.pop()
