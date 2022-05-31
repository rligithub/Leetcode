class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()

        left, right = 0, 0
        while left < len(slots1) and right < len(slots2):
            start = max(slots1[left][0], slots2[right][0])
            end = min(slots1[left][1], slots2[right][1])
            if end - start >= duration:
                return [start, start + duration]
            if slots1[left][1] < slots2[right][1]:
                left += 1
            else:
                right += 1
        return []
