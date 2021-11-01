class Solution1:
    def maxProduct(self, nums: List[int]) -> int:
        # 求最大乘积，两种cases。CASE 1:正正得正，CASE 2:负负得正。

        if not nums:
            return 0

            # CASE 1 --> if nums[i] > 0, maxvalue = maxvalue[i-1] * nums[i]
        # CASE 2 --> if nums[i] < 0, maxvalue = minvalue[i-1] * nums[i]
        # maintain two dp, maxdp and mindp, use mindp to get maxdp

        n = len(nums)
        maxdp = [0] * n
        mindp = [0] * n

        # base case
        maxdp[0] = nums[0]
        mindp[0] = nums[0]
        res = nums[0]

        for i in range(1, n):
            if nums[i] > 0:
                maxdp[i] = max(maxdp[i - 1] * nums[i], nums[i])
                mindp[i] = min(mindp[i - 1] * nums[i], nums[i])
            else:
                # 负负得正
                maxdp[i] = max(mindp[i - 1] * nums[i], nums[i])
                mindp[i] = min(maxdp[i - 1] * nums[i], nums[i])
            res = max(res, maxdp[i])
        return res


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 两种情况，case1: 正正得正 ; case2:负负得正
        # if last num at index i is positive, need to get maxproduct at index i-1
        # if last num at index i is negative, need to get minproduct at index i-1

        # corner case
        if not nums:
            return 0

        res = float('-inf')
        # create two dp
        maxdp = [0] * len(nums)
        mindp = [0] * len(nums)

        for i in range(0, len(nums)):
            # base case
            maxdp[i] = nums[i]
            mindp[i] = nums[i]
            if i > 0:  # to compare value in prev index
                maxdp[i] = max(maxdp[i], max(maxdp[i - 1] * nums[i], mindp[i - 1] * nums[i]))
                mindp[i] = min(mindp[i], min(mindp[i - 1] * nums[i], maxdp[i - 1] * nums[i]))

            res = max(res, maxdp[i])  # mindp的作用只是用来比较maxdp（负负得正的情况下maxdp是多少）
        return res


class Solution2: # 更简洁
    def maxProduct(self, nums: List[int]) -> int:
        # 正正得正，负负得正
        # base case
        if not nums:
            return 0

        # maxdp[i] -- > max product of subarray from index 0 to index i
        # mindp[i] --> min product of subarray from index 0 to index i
        n = len(nums)
        maxdp = [0] * n
        mindp = [0] * n

        # n == 1
        maxdp[0] = nums[0]
        mindp[0] = nums[0]

        # n >= 2

        for i in range(1, n):
            if nums[i] > 0:
                maxdp[i] = max(maxdp[i - 1] * nums[i], nums[i])
                mindp[i] = min(mindp[i - 1] * nums[i], nums[i])

            else:
                maxdp[i] = max(mindp[i - 1] * nums[i], nums[i])
                mindp[i] = min(maxdp[i - 1] * nums[i], nums[i])

        return max(maxdp)