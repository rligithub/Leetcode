class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # hashmap
        res = 0
        hashset = set(nums)

        for num in hashset:
            if num - 1 not in hashset:
                cur = num
                count = 1
                while cur + 1 in hashset:
                    cur += 1
                    count += 1
                res = max(res, count)
        return res 