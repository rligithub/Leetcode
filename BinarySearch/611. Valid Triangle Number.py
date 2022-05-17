class Solution1:  # TLE
    def triangleNumber(self, nums: List[int]) -> int:
        # three summ ---> similar to 259.3sum smaller
        n = len(nums)
        nums.sort()
        res = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                left, right = j + 1, n - 1

                while left <= right:
                    mid = left + (right - left) // 2
                    if nums[mid] < nums[i] + nums[j]:
                        left = mid + 1
                    else:
                        right = mid - 1
                res += right - j
        return res


