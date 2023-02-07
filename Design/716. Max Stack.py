class MaxStack:

    def __init__(self):
        self.stack = []
        self.maxx = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.maxx:
            self.maxx.append(x)
        elif self.maxx[-1] > x:
            self.maxx.append(self.maxx[-1])
        else:
            self.maxx.append(x)

    def pop(self) -> int:
        if not self.stack:
            return
        num = self.stack.pop()
        self.maxx.pop()
        return num

    def top(self) -> int:
        if not self.stack:
            return
        num = self.stack[-1]
        return num

    def peekMax(self) -> int:
        if not self.maxx:
            return
        num = self.maxx[-1]
        return num

    def popMax(self) -> int:
        num = self.peekMax()
        temp = []
        while self.top() != num:
            temp.append((self.pop()))
        self.pop()

        while temp:
            self.push(temp.pop())
        return num

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
