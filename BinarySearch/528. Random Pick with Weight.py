class Solution:

    def __init__(self, w: List[int]):
        # 为使得每个随机的数的概率为w[i]/sum[w] --> 随机数的取值为 1到 prefsum[-1] --> 每次binary search找 左边的index的概率为各个prefsum的diff
        # prefsum
        for i in range(1, len(w)):
            w[i] += w[i - 1]
        self.w = w

    def pickIndex(self) -> int:
        # select a random num between 1 and last summ --> equally pick for each, but prob == w[i] / sum[w]
        rand = random.randint(1, self.w[-1])
        return bisect.bisect_left(self.w, rand)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()