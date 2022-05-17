class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        # binary search --> max num of removable char --> check if p is subsequences of a'

        left, right = 0, len(removable)

        while left <= right:
            mid = left + (right - left) // 2
            if self.isSubsequence(s, p, mid, removable):
                left = mid + 1
            else:
                right = mid - 1
        return left - 1

    def isSubsequence(self, s, p, k, removable):

        seen = set(removable[:k])
        j = 0
        for i, ch in enumerate(s):
            if i in seen:
                continue
            if ch == p[j]:
                j += 1
                if j == len(p):
                    return True
        return False
