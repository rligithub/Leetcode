class TwoSum:

    def __init__(self):
        self.hashmap = collections.defaultdict(int)

    def add(self, number: int) -> None:
        self.hashmap[number] += 1

    def find(self, value: int) -> bool:
        for num in self.hashmap.keys():
            target = value - num
            if target != num:
                if target in self.hashmap:
                    return True
            elif self.hashmap[target] > 1:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)