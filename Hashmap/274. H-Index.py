class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # find citations[index] >= n - index

        citations.sort()
        n = len(citations)

        for i, num in enumerate(citations):
            if num >= n - i:
                return n - i

        return 0