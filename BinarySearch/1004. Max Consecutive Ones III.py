class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)

        prefsum = [0]
        for i in range(n):
            prefsum.append(prefsum[-1] + 1 - nums[i])  # 把0和1反过来 --> 存入 prefsum，这样就能知道有几个 0
        res = 0
        for j in range(1, n + 1):  # prefsum的初始0不算             # 对于任意的右端点, 希望找到最小的左端点 使得 不超过 k 个 0
            i = bisect.bisect_left(prefsum, prefsum[j] - k)
            res = max(res, j - i)
        return res
