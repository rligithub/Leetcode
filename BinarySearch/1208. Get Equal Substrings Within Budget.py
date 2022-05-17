class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # target ---> sum of diff --> substrings --> prefsum

        prefsum = [0]
        for s1, s2 in zip(s, t):
            diff = abs(ord(s1) - ord(s2))
            prefsum.append(prefsum[-1] + diff)

        # for loop each num in prefsumm --> binary search second num --> update max size each time
        res = 0
        for i in range(len(prefsum)):
            left, right = i, len(prefsum) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if prefsum[mid] - prefsum[i] <= maxCost:
                    size = mid - i
                    res = max(res, size)
                    left = mid + 1
                else:
                    right = mid - 1
        return res


