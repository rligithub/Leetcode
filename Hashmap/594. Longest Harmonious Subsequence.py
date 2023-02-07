class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # hashmap把所有数字的freq存起来,然后跳出最大的两个 并且 这两个数字是相差为1

        freq = collections.Counter(nums)

        res = 0

        for num in freq.keys():
            if num - 1 in freq:
                res = max(res, freq[num - 1] + freq[num])
            if num + 1 in freq:
                res = max(res, freq[num + 1] + freq[num])
        return res