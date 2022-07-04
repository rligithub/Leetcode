class MyStack:

    def __init__(self):
        self.queue1 = collections.deque()
        self.queue2 = collections.deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        node = self.queue1.popleft()
        while self.queue2:
            self.queue1.append(self.queue2.popleft())

        return node

    def top(self) -> int:

        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        node = self.queue1.popleft()
        self.queue2.append(node)
        while self.queue2:
            self.queue1.append(self.queue2.popleft())

        return node

    def empty(self) -> bool:

        return len(self.queue1) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()