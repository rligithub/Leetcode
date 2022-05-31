class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 一条船最多带 两人。每条船的weight limit有限，求带走所有的人，最少需要几条船
        # sort一下，每次必带people[right]，如果还有空间就带people[left]，left右移，减少 停止的条件
        count = 0
        people.sort()

        left, right = 0, len(people) - 1

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            count += 1

        return count

