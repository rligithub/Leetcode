class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:

        mod = 10 ** 9 + 7
        stack = []
        res = 0
        n = len(nums)
        prefix = [0]
        for i in range(n):
            prefix.append(prefix[i] + nums[i])
        for i in range(n):
            start = i
            while stack and stack[-1][1] > nums[i]:
                start, num = stack.pop()
                res = max(res, num * (prefix[i] - prefix[start]))

            stack.append((start, nums[i]))

        while stack:
            start, num = stack.pop()
            res = max(res, num * (prefix[n] - prefix[start]))

        return res % mod