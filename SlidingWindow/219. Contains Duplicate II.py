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