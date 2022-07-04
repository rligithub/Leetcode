class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        while True:
            a, b = random.uniform(-self.r, self.r), random.uniform(-self.r, self.r)
            if a **2 + b**2 <= self.r * self.r:
                return [self.x + a, self.y + b]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()