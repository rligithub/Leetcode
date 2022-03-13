class Solution1:
    def judgePoint24(self, cards: List[int]) -> bool:
        # permutation

        return self.dfs(cards)

    def dfs(self, nums):

        if len(nums) == 1 and abs(nums[0] - 24) <= 0.001:
            return True

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                # 先提取出两个，做操作 合并成一个数 --> 剩下两个 下一层做操作 --> 剩下一个数时比较是否为24
                base = [nums[k] for k in range(len(nums)) if k != i and k != j]

                if self.dfs(base + [nums[i] + nums[j]]): return True
                if self.dfs(base + [nums[i] * nums[j]]): return True
                if self.dfs(base + [nums[i] - nums[j]]): return True
                if self.dfs(base + [nums[j] - nums[i]]): return True
                if nums[j] != 0 and self.dfs(base + [nums[i] / nums[j]]): return True
                if nums[i] != 0 and self.dfs(base + [nums[j] / nums[i]]): return True

        return False



