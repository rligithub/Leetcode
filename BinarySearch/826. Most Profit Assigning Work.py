class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # binary search --> for loop worker, find worker's ability in difficulty --> get max profits for each worker ++

        # build graph --> combined difficulty and profit --> sort
        arr = []
        for d, p in zip(difficulty, profit):
            arr.append((d, p))

        arr.sort()
        # pre-processing --> find max profit as of current index i
        maxprofit = {}
        for i, (d, p) in enumerate(arr):
            if i == 0:
                maxprofit[i] = p
                continue
            maxprofit[i] = max(maxprofit[i - 1], p)

        # binary search find the right most difficulty task --> then take the profit which will be the result
        res = 0
        for w in worker:
            pos = self.findRightMost(arr, w)
            if pos != -1:
                res += maxprofit[pos]

        return res

    def findRightMost(self, nums, target):
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

