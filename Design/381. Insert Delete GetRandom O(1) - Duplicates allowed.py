class RandomizedCollection:

    def __init__(self):
        self.hashmap = collections.defaultdict(list)  # {num: index1, index2...}  has duplicated values
        self.arr = []

    def insert(self, val: int) -> bool:
        exist = False
        if not self.hashmap[val]:
            exist = True

        self.hashmap[val].append(len(self.arr))
        self.arr.append(val)

        return exist

    def remove(self, val: int) -> bool:
        if not self.hashmap[val]:
            return False
            # swap positions with last index, delete last position from arr, delete from hashmap
        lastNum = self.arr[-1]
        idx = self.hashmap[val][-1]
        self.arr[-1], self.arr[idx] = self.arr[idx], self.arr[-1]
        self.hashmap[lastNum].remove(len(self.arr) - 1)  # 把hashmap中的旧index删掉，replace 新的swap后的index
        self.hashmap[lastNum].append(idx)

        self.arr.pop()
        self.hashmap[val].pop()
        return True

    def getRandom(self) -> int:
        if not self.arr:
            return
        pos = random.randint(0, len(self.arr) - 1)
        return self.arr[pos]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()