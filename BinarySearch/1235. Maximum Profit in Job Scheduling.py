class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # for loop each time --> for prev assignment, binary search start time in other's end time 将所有工作按照结束时间从小到大排序，方便查找最接近当前工作的前一个工作

        # build graph --> combine starttime, endtime, profit --> sort by endtime
        n = len(startTime)
        arr = []
        dp = [0] * n
        for i in range(n):
            arr.append((endTime[i], startTime[i], profit[i]))
        arr.sort()

        # for loop each end time --> find prev end time (use binary search to search current start tiime to find prev end --> right boundary) ==> if found, dp[i] = dp[prev] + cur_profit, if not found, dp[i] = dp[prev] ==> dp[i] = max(dp[i-1], dp[i])
        for i in range(n):
            end, start, p = arr[i]
            pos = self.search(arr, start)  # find right boundary
            if pos != -1:
                dp[i] = dp[pos] + p
            else:
                dp[i] = p
            dp[i] = max(dp[i - 1], dp[i])
        return dp[-1]

    def search(self, nums, target):
        res = -1
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid][0] <= target:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res
