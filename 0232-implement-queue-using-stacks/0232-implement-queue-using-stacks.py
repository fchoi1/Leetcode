class MyQueue:

    def __init__(self):
        self.stack = []
        self.idx = 0

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        val = self.stack[self.idx]
        self.idx += 1
        return val
        

    def peek(self) -> int:
        return self.stack[self.idx]
        

    def empty(self) -> bool:
        if not self.stack:
            return True
        return len(self.stack) == self.idx


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()