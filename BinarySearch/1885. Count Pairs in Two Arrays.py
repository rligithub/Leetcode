class Solution1:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        # nums1[i] + nums1[j] > nums2[i] + nums2[j] ----> nums1[i] - nums2[i] > nums2[j] - nums1[j]
        # ===> nums1[i] - nums2[i] > - (nums1[j] - nums2[j]) ====> build a new array to store the diff

        n1, n2 = len(nums1), len(nums2)

        diff = []
        for i in range(n1):
            diff.append(nums1[i] - nums2[i])

        diff.sort()
        res = 0
        for i in range(n1):
            left, right = i + 1, n1 - 1  # find right boundary
            while left <= right:
                mid = left + (right - left) // 2
                if diff[mid] > -diff[i]:
                    right = mid - 1
                else:
                    left = mid + 1
            res += n1 - left
        return res


