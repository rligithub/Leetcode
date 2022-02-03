class Solution:
    def pathSum(self, nums: List[int]) -> int:
        # 215 --> depth, position, value --> 2nd level, 1 st position, value 5

        hashmap = collections.defaultdict(int)
        if not nums or len(nums) == 0:
            return 0

        self.res = 0
        for num in nums:
            hashmap[num // 10] = num % 10  # {(depth,position): value}
        idx = nums[0] // 10  # root's depth and position
        self.dfs(idx, 0, hashmap)
        return self.res

    def dfs(self, idx, summ, hashmap):
        depth = idx // 10
        pos = idx % 10

        left = (depth + 1) * 10 + pos * 2 - 1
        right = (depth + 1) * 10 + pos * 2
        summ = summ + hashmap[idx]

        if left not in hashmap and right not in hashmap:
            self.res += summ
            return
        if left in hashmap:
            self.dfs(left, summ, hashmap)
        if right in hashmap:
            self.dfs(right, summ, hashmap)



