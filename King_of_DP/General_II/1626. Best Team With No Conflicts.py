class Solution:  # bottom up dp
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        # 年龄越大，成绩越高，相同年龄的队员成绩没有conflict，求要怎么组队 使得整个team的累积成绩最高
        # sort by age, then sort by scores, return max sum of longest increasing subsequence

        # sorted by age
        n = len(scores)
        nums = []
        for i in range(n):
            nums.append([ages[i], scores[i]])
        nums = sorted(nums, key=lambda x: (x[0], x[1]))

        # get sum of LIS
        dp = [0] * n
        for i in range(n):
            dp[i] = nums[i][1]
            for j in range(i):
                if nums[i][1] >= nums[j][1]:
                    dp[i] = max(dp[i], dp[j] + nums[i][1])

        return max(dp)


