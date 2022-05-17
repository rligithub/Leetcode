class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:

        # woodcut --> binary search max distance --> check if can install k stations
        n = len(stations)
        diff = []
        for i in range(n - 1):
            diff.append(stations[i + 1] - stations[i])

        res = 0
        left, right = 0, max(diff)
        while left + 10 ** (-6) < right:
            mid = left + (right - left) / 2

            if self.getCount(diff, mid, k) <= k:  # less station installed --> must install more --> narrow down dist
                res = mid
                right = mid
            else:
                left = mid
        return res

    def getCount(self, nums, size, k):
        count = 0
        for num in nums:
            count += math.ceil(num / size) - 1
            if count > k:
                return count

        return count 