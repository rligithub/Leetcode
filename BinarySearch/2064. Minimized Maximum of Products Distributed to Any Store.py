class Solution1:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # binary search max num of product given --> check is it's valid

        left, right = 1, max(quantities)

        while left <= right:
            mid = left + (right - left) // 2
            if self.getCount(n, quantities, mid) <= n:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def getCount(self, n, quantities, mid):

        store = 0
        for num in quantities:
            store += math.ceil(num / mid)

        return store


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # binary search max num of product given --> check is it's valid

        left, right = 1, max(quantities)

        while left <= right:
            mid = left + (right - left) // 2
            if self.isValid(n, quantities, mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

    def isValid(self, n, quantities, mid):

        store = 0
        for num in quantities:
            store += math.ceil(num / mid)

        return store <= n