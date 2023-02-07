class Solution1:
    def hIndex(self, citations: List[int]) -> int:
        # find index with num[index] >= n - index
        # find target --> template 1

        n = len(citations)
        left, right = 0, n - 1

        while left <= right:
            mid = left + (right - left) // 2
            if citations[mid] >= n - mid:
                right = mid - 1
            else:
                left = mid + 1
        return n - left


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # find index with num[index] >= n - index

        n = len(citations)
        for i, num in enumerate(citations):
            if num >= n - i:
                return n - i
        return 0
