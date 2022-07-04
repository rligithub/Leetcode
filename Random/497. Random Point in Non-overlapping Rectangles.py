class Solution:
    # 算出每个长方形的点数， 累积相加。如果随机的数是在该长方形的点数之下，则从该长方形的位置中 随机生出点 --> 使n块田地被选中的概率与面积成正比，这样再在其中随机选苗，即可使得三块田地中的苗被选中的概率均为为 1/n*m

    def __init__(self, rects: List[List[int]]):
        self.recs = rects

    def pick(self) -> List[int]:
        curSum = 0
        idx = 0
        for i, (x1, y1, x2, y2) in enumerate(self.recs):
            cur = (x2 - x1 + 1) * (y2 - y1 + 1)
            curSum += cur
            if random.randint(0, curSum - 1) < cur:
                idx = i
        x1, y1, x2, y2 = self.recs[idx]
        return [random.randint(x1, x2), random.randint(y1, y2)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()