class MyQueue:

    def __init__(self):
        self.c, self.b = [], []

    def push(self, x: int) -> None:
        self.c.append(x)

    def pop(self) -> int:
        res = self.c[0]
        for i in range(1, len(self.c)):
            self.b.append(self.c[i])
        self.c, self.b = self.b, []
        return res

    def peek(self) -> int:
        return self.c[0]

    def empty(self) -> bool:
        return not self.c


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()