class Solution1:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        n = len(bulbs)
        if n == 0 or k >= n:
            return -1

        k += 1
        size = (n + k) // k
        lows = [float('inf') for i in range(size)]
        highs = [float('-inf') for i in range(size)]

        for i in range(n):
            x = bulbs[i]
            p = x // k
            if x < lows[p]:
                lows[p] = x
                if p > 0 and highs[p - 1] == x - k:
                    return i + 1

            if x > highs[p]:
                highs[p] = x
                if p < size - 1 and lows[p + 1] == x + k:
                    return i + 1

        return -1


from sortedcontainers import SortedList


class Solution:
    def kEmptySlots(self, bulbs, k):
        nums = SortedList()
        k += 1
        for i, bulb in enumerate(bulbs):
            pos = nums.bisect_left(bulb)
            # when a new bulb is added, we only care about the bulbs that are next to it in active (so don't insert the bulb yet)
            if (pos > 0 and bulb - nums[pos - 1] == k) or (pos < len(nums) and nums[pos] - bulb == k):
                return i + 1
            # okay, we've checked and the termination condition wasn't satisfied
            # now add in the bulb
            nums.add(bulb)
        return -1