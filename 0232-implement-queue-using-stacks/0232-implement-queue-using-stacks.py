class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def refill(self):
        while self.s2:
            self.s1.append(self.s2.pop())

    def push(self, x: int) -> None:
        self.s2.append(x)

    def pop(self) -> int:
        if not self.s1:
            self.refill()
        return self.s1.pop()
        
    def peek(self) -> int:
        if not self.s1:
            self.refill()
        return self.s1[-1]
        
    def empty(self) -> bool:
        return len(self.s1) == 0 and len(self.s2) == 0
