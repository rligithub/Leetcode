class Solution1:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:

        n = len(arr)
        left, right = 0, n - 1

        # find left stop point
        while left + 1 < n and arr[left + 1] >= arr[left]:
            left += 1

        # find right stop point
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1

        if left >= right:
            return 0
        res = min(n - left - 1, right)

        # check two non-decreasing arr can be marge together
        i, j = 0, right
        while i <= left and j <= n - 1:
            if arr[i] <= arr[j]:
                res = min(res, j - i - 1)
                i += 1
            else:
                j += 1

        return res


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        res = n - 1
        # find right stop point
        right = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1

        res = min(res, right)

        if res == 0:
            return 0

        for i in range(n):
            if i > 0 and arr[i - 1] > arr[i]:
                break
            while right < n and arr[right] < arr[i]:
                right += 1
            res = min(res, right - i - 1)
        return res