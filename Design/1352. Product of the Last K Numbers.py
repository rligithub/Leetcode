class ProductOfNumbersTLE:

    def __init__(self):
        self.nums = []

    def add(self, num: int) -> None:
        self.nums.append(num)

    def getProduct(self, k: int) -> int:

        res = 1
        for i in range(1, k + 1):
            if self.nums[-i] == 0:
                return 0
            res *= self.nums[-i]

        return res


class ProductOfNumbers:  # prefix product

    def __init__(self):
        self.nums = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.nums = [1]
        else:
            self.nums.append(self.nums[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.nums):
            return 0

        return self.nums[-1] // self.nums[-k - 1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)