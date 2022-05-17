class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        # similar to copy book

        if k > sum(ribbons):
            return 0

        res = 0
        left, right = 1, max(ribbons)

        while left <= right:
            mid = left + (right - left) // 2
            if self.numOfCuts(ribbons, mid) >= k:  # more cuts, shorter wood --> move right
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res

    def numOfCuts(self, woods, size):
        res = 0
        for wood in woods:
            res += wood // size
        return res


