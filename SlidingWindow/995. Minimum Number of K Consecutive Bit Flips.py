class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        # https://leetcode.cn/problems/minimum-number-of-k-consecutive-bit-flips/solution/hua-dong-chuang-kou-shi-ben-ti-zui-rong-z403l/
        n = len(nums)
        queue = collections.deque()  # maintain flip start points --> check size of flip, popleft if over size

        res = 0
        for i in range(n):
            if queue and i >= queue[0] + k:  # 检查上一轮的翻转是否会影响当前num
                queue.popleft()

            if len(queue) % 2 == nums[i]:  # 判断前几轮翻转的次数 影响当前num后，当前num是否还需要翻转
                if i + k > n: return -1
                queue.append(i)
                res += 1

        return res
