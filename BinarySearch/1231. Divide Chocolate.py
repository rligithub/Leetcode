class Solution1:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        # wood cut --> binary search min sweetness to you --> check if it can be cutted by k + 1 pices

        left, right = 0, sum(sweetness)
        while left <= right:
            mid = left + (right - left) // 2  # find right boundary
            if self.getPices(sweetness, mid) >= k + 1:  # more pices == less sweet --> move right
                left = mid + 1
            else:
                right = mid - 1
        return left - 1

    def getPices(self, sweetness, minsweet):

        count = 0
        summ = 0
        for num in sweetness:
            summ += num
            if summ >= minsweet:
                count += 1
                summ = 0
        return count


class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        # wood cut --> binary search min sweetness to you --> check if it can be cutted by k + 1 pices

        res = 0
        left, right = 0, sum(sweetness)
        while left <= right:
            mid = left + (right - left) // 2  # find right boundary
            if self.getPices(sweetness, mid) >= k + 1:  # more pices == less sweet --> move right .
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res

    def getPices(self, sweetness, minsweet):

        count = 0
        summ = 0
        for num in sweetness:
            summ += num
            if summ >= minsweet:
                count += 1
                summ = 0
        return count 