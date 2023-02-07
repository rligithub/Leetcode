class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        change = [0] * (n + 1)

        for i in range(n):
            change[(i + 1 + n - nums[
                i]) % n] -= 1  # move to last position (i+1), then move to i position (n - nums[i]) --> no point
            change[(i + 1) % n] += 1  # get point
        print(change)
        summ = 0
        maxScore = 0
        k = 0
        for i in range(1, n):
            summ += change[i]
            if summ > maxScore:
                maxScore = summ
                k = i

        return k