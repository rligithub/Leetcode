class Solution1:  # template 1
    def maxDistance(self, position: List[int], m: int) -> int:

        position.sort()

        # binary search --> force
        left, right = 1, position[-1] - position[0]
        while left <= right:  # find right boundary
            mid = left + (right - left) // 2
            if self.count(position, mid) >= m:  # how many balls can be placed --> more balls --> force can be higher
                left = mid + 1
            else:
                right = mid - 1
        return left - 1

    def count(self, position, force):
        # use two points to count num of balss placed
        count = 1
        i = 0
        for j in range(1, len(position)):
            if position[j] - position[i] >= force:
                count += 1
                i = j
        return count


class Solution:  # template 3
    def maxDistance(self, position: List[int], m: int) -> int:

        position.sort()

        # binary search --> force
        left, right = 1, position[-1] - position[0]
        while left + 1 < right:  # find right boundary
            mid = left + (right - left) // 2
            if self.count(position, mid) >= m:  # how many balls can be placed --> more balls --> force can be higher
                left = mid
            else:
                right = mid
        if self.count(position, left) > self.count(position, right):
            return left
        return right

    def count(self, position, force):
        # use two points to count num of balss placed
        count = 1
        i = 0
        for j in range(1, len(position)):
            if position[j] - position[i] >= force:
                count += 1
                i = j
        return count
