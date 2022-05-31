class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = m - 1
        right = n - 1
        for i in range(len(nums1) - 1, -1, -1):
            if left < 0:
                nums1[i] = nums2[right]
                right -= 1
            elif right < 0:
                nums1[i] = nums1[left]
                left -= 1
            elif nums1[left] > nums2[right]:
                nums1[i] = nums1[left]
                left -= 1
            else:
                nums1[i] = nums2[right]
                right -= 1

