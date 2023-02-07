class Solution1:  # TLE
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        for i in range(len(nums)):
            for j in range(i + 1, min(i + k + 1, len(nums))):
                if nums[i] == nums[j]:
                    return True
        return False


class Solution:  # hashmap
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        hashmap = collections.defaultdict(list)
        for i, num in enumerate(nums):
            hashmap[num].append(i)

        for num in hashmap.keys():
            if len(hashmap[num]) > 1:
                for j in range(1, len(hashmap[num])):
                    if hashmap[num][j] - hashmap[num][j - 1] <= k:
                        return True

        return False

class Solution1:  # O(n) --> hashmap
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        hashmap = {}

        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = i
            else:
                if i - hashmap[nums[i]] <= k:
                    return True
                hashmap[nums[i]] = i
        return False

class Solution:  # TLE  sliding window
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # sliding window --> size k

        n = len(nums)
        l = 0
        for r in range(1, n):
            while r - l > k:
                l += 1
            if len(set(nums[l:r + 1])) < len(nums[l:r + 1]):
                return True

        return False