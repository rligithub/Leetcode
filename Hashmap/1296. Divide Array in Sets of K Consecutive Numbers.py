class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        counter = collections.Counter(nums)
        for num in sorted(counter.keys()):
            f = counter[num]
            if f:
                for i in range(k):
                    if counter[num + i] and counter[num + i] >= f:
                        counter[num + i] -= f
                    else:
                        return False

        return True
