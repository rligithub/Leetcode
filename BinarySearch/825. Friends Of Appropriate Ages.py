class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        # 二分查找 找出 左右两边的边界，begin 为 大于 x*0.5 +7 的一个数的index，end 为 和 x相等的最后一个数的index
        # 取区间的数量，累加就是答案

        res = 0
        ages.sort()

        for i in range(len(ages) - 1, -1, -1):  # from older to younger --> ages[i] == x
            x = ages[i]
            r = self.findRightBoundary(ages, x) - 1
            l = self.findRightBoundary(ages, x * 0.5 + 7)
            if r - l >= 0:
                res += r - l
        return res

    def findRightBoundary(self, nums, target):  # find last position
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return left




import bisect

bisect.insort()