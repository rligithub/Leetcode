class Solution:
    def waysToSplit(self, nums: List[int]) -> int:

        mod = 10 ** 9 + 7
        prefsum = [0]
        for num in nums:  # has padding
            prefsum.append(prefsum[-1] + num)
        count = 0
        for i in range(1, len(prefsum)):
            if prefsum[i] * 3 > prefsum[-1]:
                break
            beg = bisect.bisect_left(prefsum, prefsum[i] * 2, i + 1, len(prefsum) - 1)
            end = bisect.bisect_right(prefsum, (prefsum[i] + prefsum[-1]) // 2, i + 1, len(prefsum) - 1)

            if end >= beg:
                count += end - beg
        return count % mod

