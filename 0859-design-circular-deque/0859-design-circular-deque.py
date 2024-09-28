class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.q = deque()

    def insertFront(self, value: int) -> bool:
        if len(self.q) == self.size:
            return False
        self.q.appendleft(value)
        return True

    def insertLast(self, value: int) -> bool:
        if len(self.q) == self.size:
            return False
        self.q.append(value)
        return True

    def deleteFront(self) -> bool:
        if self.q:
            self.q.popleft()
            return True
        return False
        
    def deleteLast(self) -> bool:
        if self.q:
            self.q.pop()
            return True
        return False
        
    def getFront(self) -> int:
        if self.q:
            return self.q[0]
        return -1
        

    def getRear(self) -> int:
        if self.q:
            return self.q[-1]
        return -1
        

    def isEmpty(self) -> bool:
        return len(self.q) == 0
        

    def isFull(self) -> bool:
        return len(self.q) == self.size

        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()