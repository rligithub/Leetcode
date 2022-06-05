class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 0

        left = 0
        maxqueue = collections.deque()
        minqueue = collections.deque()

        for i in range(len(nums)):

            # maintain max vlaue in maxqueue[0]
            while maxqueue and nums[i] > nums[maxqueue[-1]]:
                maxqueue.pop()

            # maintain min value in miinqueue[0]
            while minqueue and nums[i] < nums[minqueue[-1]]:
                minqueue.pop()

            maxqueue.append(i)
            minqueue.append(i)

            while nums[maxqueue[0]] - nums[minqueue[0]] > limit:
                left += 1
                if left > minqueue[0]:
                    minqueue.popleft()
                if left > maxqueue[0]:
                    maxqueue.popleft()

            res = max(res, i - left + 1)

        return res