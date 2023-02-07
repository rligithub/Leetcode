class CustomStack1:

    def __init__(self, maxSize: int):
        self.n = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.n:
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        buff = []
        if len(self.stack) <= k:
            while self.stack:
                buff.append(self.stack.pop() + val)
        else:
            for i in range(len(self.stack) - k):
                buff.append(self.stack.pop())
            while self.stack:
                buff.append(self.stack.pop() + val)

        while buff:
            self.stack.append(buff.pop())


class CustomStack: # use arr + stack 

    def __init__(self, maxSize: int):
        self.n = maxSize
        self.stack = []
        self.inc = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.n:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop() + self.inc.pop()
        return -1

    def increment(self, k: int, val: int) -> None:

        for i in range(min(k, len(self.stack))):
            self.inc[i] += val

        # Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)