class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # 找 product --> 分正负 --> 判断是否有k个product小于它
        # 二分一个target，看有多少个乘积<= target。数数时要遍历其中一个数组
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        a = nums1[0] * nums2[0]
        b = nums1[0] * nums2[-1]
        c = nums1[-1] * nums2[0]
        d = nums1[-1] * nums2[-1]

        left = min(a, b, c, d)
        right = max(a, b, c, d)

        while left <= right:
            mid = left + (right - left) // 2

            if self.getNumOfSmaller(nums1, nums2, k, mid) < k:
                left = mid + 1
            else:
                right = mid - 1

        return left

    def getNumOfSmaller(self, nums1, nums2, k, target):
        total = 0
        for num in nums1:
            if num > 0:
                total += bisect.bisect_right(nums2, target // num)
            if num < 0:
                total += len(nums2) - bisect.bisect_left(nums2, ceil(target / num))
            if num == 0 and target >= 0:
                total += len(nums2)

        return total


