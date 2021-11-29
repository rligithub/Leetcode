class Solution1:
    def maxScore(self, nums: List[int]) -> int:
        memo = {}
        res = self.dfs(tuple(nums), 1, memo)  # turn the input into a tuple so the function can be cached
        return res

    def dfs(self, nums, i, memo):
        if (nums, i) in memo:
            return memo[(nums, i)]

        if not nums:
            return 0

        res = float('-inf')
        # choose a as a partition
        for comb in itertools.combinations(nums, 2):
            # print(comb, comb[0])
            remain = list(nums)
            for num in comb:
                remain.remove(num)
            res = max(res, i * gcd(comb[0], comb[1]) + self.dfs(tuple(remain), i + 1, memo))

        memo[(nums, i)] = res
        return memo[(nums, i)]


class Solution1:
    def maxScore(self, nums) -> int:

        n = len(nums)
        full_mask = 1 << n - 1
        memo = {}
        return self.dfs(nums, full_mask, 1, 0, memo)

    def dfs(self, nums, fullmask, k, state, memo):
        if (k, state) in memo:
            return memo[(k, state)]

        n = len(nums)
        if state == fullmask:
            return 0

        res = 0
        for i in range(n):
            if state & (1 << i) == 0:
                for j in range(i + 1, n):
                    if state & (1 << j) == 0:
                        res = max(res, k * gcd(nums[i], nums[j]) + self.dfs(nums, fullmask, k + 1,
                                                                            state | (1 << i) | (1 << j), memo))
        memo[(k, state)] = res
        return memo[(k, state)]


class Solution3:
    def maxScore(self, nums) -> int:

        n = len(nums)
        full_mask = 1 << n - 1
        memo = {}
        return self.dfs(nums, full_mask, 1, 0, memo)

    def dfs(self, nums, fullmask, k, state, memo):
        if (k, state) in memo:
            return memo[(k, state)]

        n = len(nums)
        if state == fullmask:
            return 0

        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                if state & (1 << i) == 0 and state & (1 << j) == 0:
                    res = max(res,
                              k * gcd(nums[i], nums[j]) + self.dfs(nums, fullmask, k + 1, state | (1 << i) | (1 << j),
                                                                   memo))
        memo[(k, state)] = res
        return memo[(k, state)]


