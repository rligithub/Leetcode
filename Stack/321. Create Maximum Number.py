class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        # assume keep i digits from nums1, keep k - i digits from nums2
        # the merge two remaining nums together
        # keep i digits from nums1 ====> remove n - i digits smallest num --> similar to #402 remove k digits

        res = [0 for i in range(k)]
        n, m = len(nums1), len(nums2)

        for i in range(k + 1):
            if i > n or k - i > m:
                continue
            stack1 = self.getNums(nums1, i)
            stack2 = self.getNums(nums2, k - i)
            num = self.merge(stack1, stack2)
            res = max(res, num)

        return res

    def getNums(self, nums, k):
        stack = []
        k = len(nums) - k

        if k >= len(nums):
            return []

        for num in nums:
            while k > 0 and stack and stack[-1] < num:
                stack.pop()
                k -= 1
            stack.append(num)
        while stack and k:
            stack.pop()
            k -= 1
        return stack

    def merge(self, nums1, nums2):
        ans = []
        while nums1 or nums2:
            if nums1 > nums2:
                ans += nums1[0],
                nums1 = nums1[1:]
            else:
                ans += nums2[0],
                nums2 = nums2[1:]
        return ans



