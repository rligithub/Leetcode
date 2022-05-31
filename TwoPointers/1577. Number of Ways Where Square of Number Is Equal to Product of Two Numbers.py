class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        n1, n2 = len(nums1), len(nums2)
        nums1.sort()
        nums2.sort()

        return self.getCount(nums1, nums2, n1, n2) + self.getCount(nums2, nums1, n2, n1)

    def getCount(self, nums1, nums2, n1, n2):
        count = 0
        for i in range(n1):
            left, right = 0, n2 - 1
            while left < right:
                if nums2[left] * nums2[right] < nums1[i] * nums1[i]:
                    left += 1
                elif nums2[left] * nums2[right] > nums1[i] * nums1[i]:
                    right -= 1

                elif nums2[left] != nums2[right]:
                    newL = left
                    newR = right

                    while nums2[left] == nums2[newL]:
                        newL += 1
                    while nums2[right] == nums2[newR]:
                        newR -= 1
                    count += (newL - left) * (right - newR)
                    left = newL
                    right = newR

                else:
                    size = right - left + 1
                    count += size * (size - 1) // 2
                    break

        return count
