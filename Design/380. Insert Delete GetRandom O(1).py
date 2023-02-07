class RandomizedSet:

    def __init__(self):
        self.hashmap = {}  # {val:index}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        self.hashmap[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        lastNum = self.arr[-1]  # 把arr最后一个数 换掉 要被removed的位置，更新hashmap，然后删掉arr最后一个数
        idx = self.hashmap[val]
        self.arr[idx], self.arr[-1] = self.arr[-1], self.arr[idx]
        self.hashmap[lastNum] = idx

        self.arr.pop()
        del self.hashmap[val]
        return True

    def getRandom(self) -> int:
        if not self.arr:
            return
        pos = random.randint(0, len(self.arr) - 1)
        return self.arr[pos]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()