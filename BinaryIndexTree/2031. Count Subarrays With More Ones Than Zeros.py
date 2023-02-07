class BinaryIndexedTree:
    def __init__(self, n):
        self.freq = [0] * (n + 1)

    def lowbit(self, x):
        return x & (-x)

    def update(self, i, val):
        while i < len(self.freq):
            self.freq[i] += val
            i += self.lowbit(i)

    def query(self, i):
        res = 0
        while i > 0:
            res += self.freq[i]
            i -= self.lowbit(i)
        return res


class Solution1:  # BIT + index need to be positive, so find value as (any sum - minnsum) in tree
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        prefsum = [0]

        for num in nums:
            if num == 0:
                prefsum.append(prefsum[-1] + (-1))
            else:
                prefsum.append(prefsum[-1] + num)

        maxxSum = max(prefsum)
        minnSum = min(prefsum)
        tree = BinaryIndexedTree(maxxSum - minnSum + 1)

        res = 0
        mod = 10 ** 9 + 7
        for sum1 in prefsum:  # sum1 - sum2 > 0 ----> sum2 < sum1
            res += tree.query(sum1 - minnSum)
            tree.update(sum1 - minnSum + 1, 1)
            print(prefsum, sum1, tree.freq)
        return res % mod


class Solution:  # compress nums + BIT
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        # similar to 315. Count of smaller numbers after self -----> sum1 - sum2 > 0 ==> sum1 > sum2
        # get prefSum
        prefsum = [0]
        for num in nums:
            if num == 0:
                prefsum.append(prefsum[-1] + (-1))
            else:
                prefsum.append(prefsum[-1] + num)

        # sort prefsum
        sortedSum = sorted(list(set(prefsum)))
        # compress sorted prefsum and save index
        index = {}
        for i, num in enumerate(sortedSum):
            index[num] = i + 1

        # operation --> find sum1 > sum2
        mod = 10 ** 9 + 7
        res = 0
        tree = BinaryIndexedTree(len(prefsum))
        for i in range(len(prefsum)):
            res += tree.query(index[prefsum[i]] - 1)
            tree.update(index[prefsum[i]], 1)
        return res % mod
