class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        # binary search num of day need --> check if there is enough flowers to make bouquets (k flower each bouquet, need m bouquet)

        if len(bloomDay) < m * k:  # no enough flowers to make bouquets
            return -1

        left, right = min(bloomDay), max(bloomDay)
        while left <= right:
            mid = left + (right - left) // 2
            if self.canMakeBouquest(bloomDay, m, k, mid):  # find left boundary
                right = mid - 1
            else:
                left = mid + 1
        return left

    def canMakeBouquest(self, bloomDay, m, k, day):

        count = 0
        curflower = 0
        for num in bloomDay:
            if num > day:
                curflower = 0
            else:
                curflower += 1
            if curflower == k:
                count += 1
                curflower = 0

        return count >= m


class Solution1:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        # binary search num of day need --> check if there is enough flowers to make bouquets (k flower each bouquet, need m bouquet)

        if len(bloomDay) < m * k:  # no enough flowers to make bouquets
            return -1
        left, right = 1, max(bloomDay)
        while left <= right:
            mid = left + (right - left) // 2
            if self.canMakeBouquest(bloomDay, k, mid) >= m:  # find left boundary
                right = mid - 1
            else:
                left = mid + 1
        return left

    def canMakeBouquest(self, bloomDay, k, day):

        count = 0
        curflower = 0
        for num in bloomDay:
            if num > day:
                curflower = 0
            else:
                curflower += 1
                if curflower == k:
                    count += 1
                    curflower = 0

        return count

