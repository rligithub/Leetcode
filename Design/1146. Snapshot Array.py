class SnapshotArray:

    def __init__(self, length: int):
        self.screen = []
        self.num = {}

    def set(self, index: int, val: int) -> None:
        self.num[index] = val

    def snap(self) -> int:
        self.screen.append(self.num.copy())
        return len(self.screen) - 1

    def get(self, index: int, snap_id: int) -> int:
        if index in self.screen[snap_id]:
            return self.screen[snap_id][index]
        else:
            return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)