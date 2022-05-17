class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1.sort()
        nums2.sort()
        visited = set()
        res = []
        if len(nums1) <= len(nums2):
            for num in nums1:
                if num in visited:
                    continue
                visited.add(num)
                if self.findNum(nums2, num):
                    res.append(num)

        else:
            for num in nums2:
                if num in visited:
                    continue
                visited.add(num)
                if self.findNum(nums1, num):
                    res.append(num)

        return res

    def findNum(self, nums, target):
        # find target
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1.sort()
        nums2.sort()
        visited = set()
        res = []
        if len(nums1) <= len(nums2):
            return self.binarySearch(nums1, nums2, visited, res)
        else:
            return self.binarySearch(nums2, nums1, visited, res)

    def binarySearch(self, nums1, nums2, visited, res):
        # find target
        for num in nums1:
            if num in visited:
                continue
            visited.add(num)
            flag = False
            left, right = 0, len(nums2) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums2[mid] == num:
                    flag = True
                    break
                elif nums2[mid] > num:
                    right = mid - 1
                else:
                    left = mid + 1
            if flag == True:
                res.append(num)
        return res