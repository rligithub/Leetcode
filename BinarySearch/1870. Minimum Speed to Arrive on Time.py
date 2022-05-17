class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # copy book --> binary search min speed, check if total hours <= hours

        # base case --> if prev stops > hour --> return -1
        if len(dist) - 1 >= hour:
            return -1

        left, right = 1, 10 ** 7

        while left <= right:
            mid = left + (right - left) // 2
            if self.getHours(dist, mid, hour) <= hour:  # less hour, higher speed -->  move to left to lower speed
                right = mid - 1
            else:
                left = mid + 1
        return left

    def getHours(self, dist, speed, hour):
        count = 0
        for i in range(len(dist)):
            if i == len(dist) - 1:
                count += dist[i] / speed
                continue
            count += math.ceil(dist[i] / speed)
            if count > hour:
                return count
        return count