class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 维持max value在左端点
        # 每进来一个数，检查是否比右端点的数大，是的话 可以移除左边的数字
        # 每次再检查下 size

        queue = collections.deque()
        res = []

        for i in range(len(nums)):
            # remove - if size is exceed
            if queue and i - queue[0] >= k:
                queue.popleft()
            # maintain max value in queue[0]
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()

            queue.append(i)

            if i >= k - 1:
                res.append(nums[queue[0]])
        return res 