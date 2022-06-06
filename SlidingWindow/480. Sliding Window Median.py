class Solution1: # two pointers
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        left = 0
        right = left + k - 1
        res = []

        while right < len(nums):
            arr = nums[left:right + 1]
            arr.sort()

            if len(arr) % 2 == 0:
                mid = k // 2
                median = (arr[mid] + arr[mid - 1]) / 2
                res.append(median)
            else:
                median = arr[k // 2]
                res.append(median)

            left += 1
            right += 1

        return res
