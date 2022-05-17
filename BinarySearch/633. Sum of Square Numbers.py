class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        maxx = int(math.sqrt(c))

        for i in range(0, maxx + 1):
            left, right = i, maxx

            while left <= right:
                mid = left + (right - left) // 2
                if i ** 2 + mid ** 2 == c:
                    return True
                elif i ** 2 + mid ** 2 > c:
                    right = mid - 1
                else:
                    left = mid + 1
        return False