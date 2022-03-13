import collections
class Solution:
    def minTransfers(self, transactions):
        self.res = float('inf')
        person = collections.defaultdict(int)
        for x, y, money in transactions:
            person[x] -= money
            person[y] += money

        debt = []
        for amount in person.values():
            if amount != 0:
                debt.append(amount)
        if not debt: # early return 
            return 0
        print('debt:', debt, 'person:', person)
        self.dfs(debt, 0, 0)
        return self.res

    def dfs(self, nums, pos, count):

        if pos == len(nums):
            self.res = min(self.res, count)
            return

        if nums[pos] == 0:
            self.dfs(nums, pos + 1, count)

        for j in range(pos + 1, len(nums)):  # person j , different person
            if nums[pos] * nums[j] < 0:  # 一正一负
                nums[j] += nums[pos]  # 把pos上的钱 摊到后面的j上，相当于处理完了pos，然后后面的人继续摊
                self.dfs(nums, pos + 1, count + 1)
                nums[j] -= nums[pos]

nums = [[0,1,10],[2,0,5]]
a = Solution()

print(a.minTransfers(nums))