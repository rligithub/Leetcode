class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # prefix summ + hashmap --> hashmap[prefsumm] = index

        prefsum = 0
        maxx = 0
        hashmap = collections.defaultdict(list)

        for i, num in enumerate(nums):
            prefsum += num
            if prefsum == k:
                maxx = i + 1

            if prefsum - k in hashmap:
                maxx = max(maxx, i - hashmap[prefsum - k])

            if prefsum not in hashmap:
                hashmap[prefsum] = i
        return maxx
