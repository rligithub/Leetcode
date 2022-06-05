class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        presum = [0]
        for i in range(len(nums)):
            presum.append(presum[-1] + nums[i])

        queue = collections.deque()
        res = float('inf')

        for i in range(len(presum)):
            while queue and presum[i] - presum[queue[0]] >= k:
                res = min(res, i - queue[0])
                queue.popleft()
            # maintain min value in queue[0]
            while queue and presum[i] <= presum[queue[-1]]:
                queue.pop()

            queue.append(i)

        if res == float('inf'):
            return -1
        return res
