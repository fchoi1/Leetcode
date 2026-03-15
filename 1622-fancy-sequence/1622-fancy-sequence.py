mod = 10 ** 9 + 7

class Fancy:

    def __init__(self):
        self.inverse = []  # (inverse of curr mul, inc)
        self.mult = 1
        self.add = 0

    def append(self, val: int) -> None:
        self.inverse.append((val - self.add) * pow(self.mult, -1, mod))

    def addAll(self, inc: int) -> None:
        self.add += inc

    def multAll(self, m: int) -> None:
        self.mult = (self.mult * m) % mod
        self.add = (self.add * m) % mod
        
    def getIndex(self, idx: int) -> int:
        if idx >= len(self.inverse):
            return -1
        
        return int(self.mult * self.inverse[idx] + self.add) % mod


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)