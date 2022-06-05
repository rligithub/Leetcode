class Solution:  # dp + deque
    def maxResult(self, nums: List[int], k: int) -> int:
        # dp[i] = max(dp[j]) + nums[i] --> j is between i - 1 and i - k

        dp = [nums[0]] + [0] * (len(nums) - 1)

        queue = collections.deque([0])
        res = float('-inf')

        for i in range(1, len(nums)):
            while queue and i - queue[0] > k:
                queue.popleft()

            dp[i] = dp[queue[0]] + nums[i]

            # maintain max dp[i]
            while queue and dp[i] >= dp[queue[-1]]:
                queue.pop()

            queue.append(i)

        return dp[-1]

