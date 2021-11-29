class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        # similar to #1066 campis Bikes II
        # for loop nums1 to try nums2--> nums2 can be rearranged
        # nums2 --> 0000 --->1111 selected

        memo = {}
        return self.dfs(nums1, nums2, 0, 0, memo)

    def dfs(self, nums1, nums2, i, state, memo):
        if (i, state) in memo:
            return memo[(i, state)]

        if i == len(nums1):
            return 0

        res = float('inf')
        for j in range(len(nums2)):
            if state & (1 << j) == 0:
                res = min(res, self.dfs(nums1, nums2, i + 1, state | (1 << j), memo) + (nums1[i] ^ nums2[j]))

        memo[(i, state)] = res
        return memo[(i, state)]